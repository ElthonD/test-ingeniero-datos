
# 🧠 Test en Línea para Ingenieros de Datos

Esta aplicación en Streamlit permite evaluar habilidades clave en arquitectura de datos, fuentes, ingesta, procesamiento, almacenamiento (SQL) y Python.

---

## 🚀 Descripción General

La aplicación está dividida en dos módulos:

- **Módulo de Test:** Para usuarios registrados. Presentan un test dividido en 5 bloques con cronómetro (60 min).
- **Módulo de Admin:** Visualiza resultados, reintentos, cambios de pestaña por bloque, y permite registrar nuevos usuarios.

---

## 👥 Usuarios de Prueba

| Nombre            | Usuario        | Contraseña             | Rol     |
|-------------------|----------------|-------------------------|---------|
| Ricardo Polo      | ricardo.polo   | R1c4rd0#2025!           | usuario |
| Osvaldo Esparza   | osvaldo.esparza| 0sp4rzA#2025!           | usuario |
| Daniel Rivas      | daniel.rivas   | S3gura#D4nR!v@s2025     | usuario |
| Administrador     | admin          | Adm1n#2025!             | admin   |

---

## 🗂 Estructura del Proyecto

- `main.py`: Lógica principal de login/redirección.
- `app.py`: Test interactivo con bloques, cronómetro y seguimiento de pestañas.
- `admin.py`: Panel de administración para ver resultados y gestionar usuarios.
- `database.db`: Base de datos SQLite con usuarios, resultados, preguntas y reintentos.
- `README.md`: Instrucciones del proyecto.

---

## 🧪 Evaluación

- 5 bloques (Fuentes de datos, Ingesta, Procesamiento, SQL, Python)
- 75 preguntas (15 por bloque, baja, media y alta dificultad)
- Cronómetro: 60 minutos
- Registro de reintentos y cambios de pestaña por bloque
- Resultados ponderados por bloque (20% c/u)

---

## 🧰 Requisitos

- Python 3.9+
- Streamlit
- Pandas, SQLite3, bcrypt

---

## ☁️ Despliegue

Puedes desplegarlo fácilmente en [Streamlit Cloud](https://streamlit.io/cloud) o localmente.

