
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

| Nombre     | Usuario         | Contraseña  | Rol     |
|------------|------------------|-------------|---------|
| Admin      | `admin`          | `Admin!2024#Secure`  | admin   |
| Ricardo    | `ricardo.polo`   | `Ricardo_2024$Test`| usuario |
| Osvaldo    | `osvaldo.esparza`| `Osvaldo@2024#Safe`| usuario |

---

## 📁 Archivos clave

- `main.py`: Login y redirección por rol
- `app.py`: Evaluación para usuarios
- `admin.py`: Panel de control para administrador
- `database.db`: Base de datos con usuarios, preguntas y resultados

---

## 🔒 Seguridad

Las contraseñas están hasheadas usando `bcrypt`.

---

## 📌 Autor

Desarrollado para pruebas técnicas de ingeniería de datos.
