import sqlite3
import bcrypt

DB = 'database.db'
usuario = 'admin'
nombre = 'Administrador'
apellido = 'Admin'
password = 'Adm1n#2025!'
rol = 'admin'

conn = sqlite3.connect(DB)
cursor = conn.cursor()
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
try:
    cursor.execute("DELETE FROM usuarios WHERE usuario = ?", (usuario,))
    cursor.execute("INSERT INTO usuarios (nombre, apellido, usuario, contraseña, rol) VALUES (?, ?, ?, ?, ?)",
                   (nombre, apellido, usuario, hashed, rol))
    conn.commit()
    print('Usuario admin creado correctamente.')
except Exception as e:
    print(f'Error al crear admin: {e}')
conn.close()
