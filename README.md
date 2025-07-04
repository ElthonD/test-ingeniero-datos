# 🧪 Test en Línea para Ingenieros de Datos

Esta aplicación permite realizar una evaluación técnica para ingenieros de datos, estructurada en 5 bloques temáticos:

1. **Fuentes de Datos**
2. **Capa de Ingesta**
3. **Capa de Procesamiento**
4. **SQL**
5. **Python**

Incluye autenticación con roles, cronómetro, registro de cambios de pestaña, y módulo administrador para visualizar resultados y registrar nuevos usuarios.

---

## 🚀 Despliegue en Streamlit Cloud

Haz clic en el siguiente botón para desplegar la app en Streamlit Cloud:

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)

> ⚠️ Asegúrate de subir todos los archivos de este repositorio, incluyendo `database.db`.

---

## 🛠️ Requisitos

- Python 3.8+
- Streamlit
- bcrypt
- pandas
- sqlite3

Instala dependencias con:

```bash
pip install -r requirements.txt
```

---

## 🧑‍💻 Usuarios Iniciales

| Nombre     | Usuario           | Contraseña             | Rol     |
|------------|-------------------|-------------------------|---------|
| Admin      | `admin`           | `Admin!2024#Secure`     | admin   |
| Ricardo    | `ricardo.polo`    | `Ricardo_2024$Test`     | usuario |
| Osvaldo    | `osvaldo.esparza` | `Osvaldo@2024#Safe`     | usuario |

---

## 📁 Archivos clave

- `main.py`: Login y redirección por rol
- `app.py`: Evaluación para usuarios
- `admin.py`: Panel de control para administrador
- `database.db`: Base de datos con usuarios, preguntas y resultados
- `requirements.txt`: Dependencias necesarias
- `README.md`: Instrucciones del proyecto

---

## 🔒 Seguridad

Las contraseñas están hasheadas usando `bcrypt` y no se almacenan en texto plano.

---

## 📌 Autor

Desarrollado para pruebas técnicas de ingeniería de datos.

---

## ❓ Preguntas Frecuentes (FAQ)

### ¿Cómo agrego nuevas preguntas al test?

Actualmente las preguntas están almacenadas en la tabla `preguntas` de `database.db`. Puedes agregarlas con cualquier visor SQLite o usando código Python como:

```python
import sqlite3

conn = sqlite3.connect("database.db")
conn.execute("INSERT INTO preguntas (bloque, nivel, pregunta, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
             ("bloque_1", "media", "¿Qué es una API REST?", "Una base de datos", "Un modelo de datos", "Una interfaz de comunicación", "Un conector SQL", "c"))
conn.commit()
conn.close()
```

### ¿Cómo agrego más usuarios desde el administrador?

Desde el panel admin, completa el formulario con:
- Nombre
- Apellido
- Nombre de usuario único
- Contraseña

Se guardarán automáticamente en la base de datos.

### ¿Cómo restablezco una contraseña?

Debes acceder a la base de datos y actualizar el campo `contraseña` del usuario deseado con un nuevo hash usando `bcrypt`.

---

¿Tienes más dudas o sugerencias? Crea un issue en tu repositorio o extiende esta guía.
