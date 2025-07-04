import streamlit as st
import pandas as pd
import sqlite3
import time
from datetime import datetime
import streamlit.components.v1 as components

DB = "database.db"

def obtener_preguntas_por_bloque(bloque):
    conn = sqlite3.connect(DB)
    df = pd.read_sql_query(f"SELECT * FROM preguntas WHERE bloque = '{bloque}'", conn)
    conn.close()
    return df

def registrar_resultados(usuario, bloque, respuestas_correctas, cambios_tabs, reintento):
    conn = sqlite3.connect(DB)
    fecha = datetime.now().strftime('%Y-%m-%d')
    conn.execute("INSERT INTO resultados (usuario, bloque, resultado, cambios_tabs, reintento, fecha) VALUES (?, ?, ?, ?, ?, ?)",
                 (usuario, bloque, respuestas_correctas, cambios_tabs, reintento, fecha))
    conn.commit()
    conn.close()

def obtener_reintentos(usuario):
    conn = sqlite3.connect(DB)
    df = pd.read_sql_query(f"SELECT COUNT(*) as total FROM resultados WHERE usuario = '{usuario}'", conn)
    conn.close()
    return int(df['total'].values[0] // 5)

def run():
    st.title("🧪 Evaluación para Ingenieros de Datos")
    usuario = st.session_state["usuario"]

    if 'test_iniciado' not in st.session_state:
        st.markdown("### Bienvenido al test de Ingeniería de Datos.")
        st.info("""
El test consta de 5 bloques temáticos:

1. **Fuentes de Datos**: APIs, SQL, CDC, datos no estructurados.
2. **Capa de Ingesta**: Kafka, arquitectura batch/streaming.
3. **Capa de Procesamiento**: Spark, Flink, GCP.
4. **SQL**: Consultas de distintas complejidades.
5. **Python**: Lógica, estructuras, funciones.

Tendrás 60 minutos para completar el test. Se registrará la cantidad de veces que cambies de pestaña durante cada bloque.

Haz clic en 'Iniciar Test' para comenzar.
""")
        if st.button("🚀 Iniciar Test"):
            st.session_state['test_iniciado'] = True
            st.session_state['start_time'] = time.time()
            st.experimental_rerun()
        st.stop()

    tiempo_transcurrido = time.time() - st.session_state['start_time']
    tiempo_restante = max(0, 60*60 - tiempo_transcurrido)
    st.markdown(f"⏰ Tiempo restante: `{int(tiempo_restante//60)} min {int(tiempo_restante%60)} seg`")

    if tiempo_restante <= 0:
        st.warning("Tiempo agotado.")
        st.stop()

    components.html("""
    <script>
    let count = 0;
    document.addEventListener("visibilitychange", function() {
        if (document.hidden) {
            count += 1;
            window.parent.postMessage({ type: 'tab_switch', value: count }, "*");
        }
    });
    </script>
    """, height=0)

    total_final = 0
    for bloque in ["fuentes_datos", "ingesta", "procesamiento", "sql", "python"]:
        st.subheader(f"🧩 Bloque: {bloque.upper().replace('_', ' ')}")
        preguntas = obtener_preguntas_por_bloque(bloque)
        correctas = 0
        cambios_tabs = st.number_input(f"Cambios de pestaña en bloque {bloque}", min_value=0, step=1, key=f"tabs_{bloque}")
        for i, row in preguntas.iterrows():
            respuesta = st.radio(row['pregunta'], eval(row['opciones']), key=f"{bloque}_{i}")
            if respuesta == row['respuesta_correcta']:
                correctas += 1
        resultado = int((correctas / len(preguntas)) * 100)
        total_final += resultado * 0.20
        reintento = obtener_reintentos(usuario)
        if st.button(f"Guardar bloque {bloque}"):
            registrar_resultados(usuario, bloque, resultado, cambios_tabs, reintento)
            st.success(f"✅ Puntaje bloque {bloque}: {resultado}/100 (reintento #{reintento + 1})")

    st.markdown(f"### 🎯 Resultado final estimado: {int(total_final)} / 100")


    


    if st.button("Cerrar sesión 🔒"):
        st.session_state.clear()
        st.success("👋 Has cerrado sesión exitosamente. ¡Gracias por usar la plataforma!")
        st.experimental_rerun()
