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
            st.rerun()
        st.stop()

    tiempo_transcurrido = time.time() - st.session_state['start_time']
    tiempo_restante = max(0, 60*60 - tiempo_transcurrido)
    st.markdown(f"⏰ Tiempo restante: `{int(tiempo_restante//60)} min {int(tiempo_restante%60)} seg`")

    if tiempo_restante <= 0:
        st.warning("Tiempo agotado.")
        st.stop()

    import streamlit.components.v1 as components
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

    # Contador de cambios de pestaña por bloque, invisible para el usuario
    if 'tab_switch_count' not in st.session_state:
        st.session_state['tab_switch_count'] = 0
    if 'tab_switch_count_prev' not in st.session_state:
        st.session_state['tab_switch_count_prev'] = 0

    # Script JS para contar cambios de pestaña y guardar en localStorage
    components.html("""
    <script>
    let count = Number(localStorage.getItem('tab_switch_count') || 0);
    document.addEventListener("visibilitychange", function() {
        if (document.hidden) {
            count += 1;
            localStorage.setItem('tab_switch_count', count);
        }
    });
    window.addEventListener("message", function(event) {
        if (event.data && event.data.type === 'get_tab_switch_count') {
            const count = Number(localStorage.getItem('tab_switch_count') || 0);
            window.parent.postMessage({type: 'tab_switch_count', value: count}, '*');
        }
    });
    </script>
    """, height=0)

    # --- NUEVO FLUJO: Mostrar todas las preguntas, guardar todo al final ---
    bloques = ["fuentes_datos", "ingesta", "procesamiento", "sql", "python"]
    preguntas_dict = {}
    for bloque in bloques:
        preguntas = obtener_preguntas_por_bloque(bloque)
        if preguntas.empty or len(preguntas) == 0:
            st.info(f"No hay preguntas registradas para el bloque '{bloque}'.")
            continue
        st.subheader(f"🧩 Bloque: {bloque.upper().replace('_', ' ')}")
        preguntas_dict[bloque] = []
        for i, row in preguntas.iterrows():
            opciones = eval(row['opciones']) if isinstance(row['opciones'], str) else row['opciones']
            respuesta = st.radio(row['pregunta'], opciones, key=f"{bloque}_{i}")
            preguntas_dict[bloque].append({
                'pregunta': row['pregunta'],
                'respuesta_correcta': row['respuesta_correcta'],
                'respuesta_usuario': respuesta
            })

    if st.button("Enviar preguntas y finalizar test"):
        import streamlit as __st
        import time as __time
        # Pedir el valor a JS
        components.html("""
        <script>
        window.parent.postMessage({type: 'get_tab_switch_count'}, '*');
        </script>
        """, height=0)
        __time.sleep(0.2)
        cambios_tabs_total = __st.session_state.get('tab_switch_count', 0)
        __st.session_state['tab_switch_count_prev'] = cambios_tabs_total
        reintento = obtener_reintentos(usuario)
        for bloque in preguntas_dict:
            preguntas_bloque = preguntas_dict[bloque]
            correctas = sum(1 for p in preguntas_bloque if p['respuesta_usuario'] == p['respuesta_correcta'])
            total_preguntas = len(preguntas_bloque)
            resultado = int((correctas / total_preguntas) * 100) if total_preguntas > 0 else 0
            registrar_resultados(usuario, bloque, resultado, cambios_tabs_total, reintento)
        st.success("¡Test finalizado! Tus respuestas han sido registradas. Muchas gracias por participar.")
        st.balloons()
        # Cerrar sesión correctamente
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    # El resultado final estimado ya no se muestra al usuario, solo se registra en la base de datos y se visualiza en el módulo admin


    


    if st.button("Cerrar sesión 🔒"):
        st.session_state.clear()
        st.success("👋 Has cerrado sesión exitosamente. ¡Gracias por usar la plataforma!")
        st.rerun()
