import streamlit as st
import pandas as pd
import sqlite3
import bcrypt
from datetime import datetime

DB = "database.db"

def run():
    if "usuario" not in st.session_state or st.session_state.get("rol") != "admin":
        st.error("🔐 Acceso restringido. Por favor inicia sesión como administrador.")
        st.stop()

    st.title("📊 Panel de Administración")

    # Conexión abierta durante toda la ejecución
    conn = sqlite3.connect(DB)

    st.subheader("📄 Resultados de Evaluaciones")
    try:
        resultados = pd.read_sql_query("SELECT * FROM resultados", conn)
        if not resultados.empty:
            df_pivot = resultados.pivot_table(index='usuario', columns='bloque', values='resultado', aggfunc='max').fillna(0)
            cambios = resultados.pivot_table(index='usuario', columns='bloque', values='cambios_tabs', aggfunc='max').fillna(0)
            reintentos = resultados.groupby('usuario')['reintento'].max()
            final = df_pivot.sum(axis=1) * 0.20
            df_pivot.columns = [f"Resultado {c}" for c in df_pivot.columns]
            cambios.columns = [f"Cambios pestaña {c}" for c in cambios.columns]
            resumen = pd.concat([df_pivot, cambios], axis=1)
            resumen["Reintentos"] = reintentos
            resumen["Resultado Final"] = final.astype(int)

            # Nueva columna: Total de cambios de pestaña en todo el test
            total_cambios = resultados.groupby('usuario')['cambios_tabs'].sum()
            resumen["Total Cambios de Pestaña"] = total_cambios

            st.dataframe(resumen)
        else:
            st.info("Aún no hay resultados.")
    except Exception as e:
        st.error(f"Error al cargar resultados: {e}")

    st.subheader("➕ Registrar nuevo usuario")
    with st.form("registro_usuario", clear_on_submit=True):
        nombre = st.text_input("Nombre")
        apellido = st.text_input("Apellido")
        nuevo_usuario = st.text_input("Usuario nuevo")
        nueva_pass = st.text_input("Contraseña nueva", type="password")
        submitted = st.form_submit_button("Registrar")

        if submitted:
            if not (nombre and apellido and nuevo_usuario and nueva_pass):
                st.warning("Todos los campos son obligatorios.")
            else:
                cursor = conn.execute("SELECT COUNT(*) FROM usuarios WHERE usuario = ?", (nuevo_usuario,))
                existe = cursor.fetchone()[0]
                if existe:
                    st.error("❌ El nombre de usuario ya está registrado.")
                else:
                    hashed = bcrypt.hashpw(nueva_pass.encode(), bcrypt.gensalt()).decode()
                    try:
                        conn.execute("INSERT INTO usuarios (nombre, apellido, usuario, contraseña, rol) VALUES (?, ?, ?, ?, 'usuario')",
                                    (nombre, apellido, nuevo_usuario, hashed))
                        conn.commit()
                        st.success(f"✅ Usuario '{nuevo_usuario}' registrado correctamente.")
                        st.experimental_rerun()
                    except Exception as e:
                        st.error(f"⚠️ Error inesperado: {e}")

    st.subheader("👥 Usuarios Registrados")
    try:
        usuarios_df = pd.read_sql_query("SELECT nombre, apellido, usuario, rol FROM usuarios", conn)
        st.dataframe(usuarios_df)
    except Exception as e:
        st.error(f"Error al mostrar usuarios: {e}")

    if st.button("Cerrar sesión 🔒"):
        st.session_state.clear()
        st.success("👋 Has cerrado sesión exitosamente.")
        st.experimental_rerun()


    st.subheader("🔁 Reiniciar Test de Usuario")
    usuarios_lista = [row[0] for row in conn.execute("SELECT DISTINCT usuario FROM resultados").fetchall()]
    if usuarios_lista:
        usuario_seleccionado = st.selectbox("Selecciona un usuario para reiniciar test", usuarios_lista)
        if st.button("Reiniciar test"):
            conn.execute("DELETE FROM resultados WHERE usuario = ?", (usuario_seleccionado,))
            conn.commit()
            st.success(f"✅ Test de '{usuario_seleccionado}' reiniciado correctamente.")
    else:
        st.info("No hay usuarios con resultados aún.")


    conn.close()