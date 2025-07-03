import streamlit as st
import sqlite3
import bcrypt
import app
import admin

DB = "database.db"

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

st.title("🔐 Portal de Evaluación para Ingenieros de Datos")

usuario = st.text_input("Usuario")
password = st.text_input("Contraseña", type="password")

if st.button("Ingresar"):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT rol, contraseña FROM usuarios WHERE usuario = ?", (usuario,))
    result = cursor.fetchone()
    conn.close()

    if result:
        rol, stored_hash = result
        if verify_password(password, stored_hash.encode()):
            st.session_state["usuario"] = usuario
            st.session_state["rol"] = rol

            if rol == "admin":
                st.success("Bienvenido, administrador.")
                admin.run()
            else:
                st.success("Bienvenido al test.")
                app.run()
        else:
            st.error("Contraseña incorrecta.")
    else:
        st.error("Usuario no encontrado.")