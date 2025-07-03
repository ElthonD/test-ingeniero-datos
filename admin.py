import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

DB = "database.db"

def run():
    st.title("📊 Panel de Administración")

    conn = sqlite3.connect(DB)

    st.subheader("📄 Resultados de Evaluaciones")
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
        st.dataframe(resumen)
    else:
        st.info("Aún no hay resultados.")

    st.subheader("➕ Registrar nuevo usuario")
    nombre = st.text_input("Nombre")
    apellido = st.text_input("Apellido")
    nuevo_usuario = st.text_input("Usuario nuevo")
    nueva_pass = st.text_input("Contraseña nueva", type="password")
    if st.button("Registrar"):
        import bcrypt
        hashed = bcrypt.hashpw(nueva_pass.encode(), bcrypt.gensalt()).decode()
        try:
            conn.execute("INSERT INTO usuarios (nombre, apellido, usuario, contraseña, rol) VALUES (?, ?, ?, ?, 'usuario')",
                         (nombre, apellido, nuevo_usuario, hashed))
            conn.commit()
            st.success("Usuario registrado correctamente.")
        except:
            st.error("Error: usuario ya existe.")
    conn.close()