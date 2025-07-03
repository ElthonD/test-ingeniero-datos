# 📊 Test de Evaluación para Ingenieros de Datos

Este proyecto es una aplicación construida en Streamlit para evaluar conocimientos clave de un ingeniero de datos en cinco bloques temáticos:

1. **Fuentes de Datos**
2. **Capa de Ingesta**
3. **Procesamiento**
4. **SQL**
5. **Python**

---

## 🧠 Características

- Autenticación de usuarios (SQLite)
- Registro de cambios de pestaña durante el test
- Puntaje por bloque y cálculo ponderado (20% cada bloque)
- Detección de reintentos
- Panel administrador para visualizar resultados y registrar nuevos usuarios

---

## 📦 Estructura del Repositorio

```
.
├── app.py               # Módulo de test del usuario
├── admin.py             # Módulo de administración
├── database.db          # Base de datos SQLite
├── requirements.txt     # Dependencias necesarias
├── schema.sql           # Script de creación de tablas
├── README.md            # Este archivo
```

---

## 🚀 Despliegue Rápido en Streamlit Cloud

Puedes lanzar esta aplicación en la nube con un clic:

### 🎯 App de Usuario

[![Abrir en Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)

### 🛠️ App de Admin

Cambia el archivo principal a `admin.py` al crear una segunda app.

---

## 🔐 Usuarios Iniciales

| Usuario         | Contraseña  | Rol     |
|----------------|-------------|---------|
| admin           | admin123    | admin   |
| ricardo.polo    | ricardo123  | usuario |
| osvaldo.esparza | osvaldo123  | usuario |

---

## 🛠️ Tecnologías Utilizadas

- Streamlit
- SQLite3
- Pandas
- HTML + JS para detección de pestañas

---

## 📥 Instalación local

```bash
pip install -r requirements.txt
streamlit run app.py
```

Para ingresar como admin:

```bash
streamlit run admin.py
```