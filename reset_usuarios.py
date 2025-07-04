import sqlite3
import bcrypt

DB = 'database.db'
usuarios = [
    {
        'usuario': 'ricardo.polo',
        'nombre': 'Ricardo',
        'apellido': 'Polo',
        'password': 'R1c4rd0#2025!',
        'rol': 'usuario'
    },
    {
        'usuario': 'osvaldo.esparza',
        'nombre': 'Osvaldo',
        'apellido': 'Esparza',
        'password': '0sp4rzA#2025!',
        'rol': 'usuario'
    },
    {
        'usuario': 'daniel.rivas',
        'nombre': 'Daniel',
        'apellido': 'Rivas',
        'password': 'S3gura#D4nR!v@s2025',
        'rol': 'usuario'
    }
]

conn = sqlite3.connect(DB)
cursor = conn.cursor()
for u in usuarios:
    hashed = bcrypt.hashpw(u['password'].encode(), bcrypt.gensalt()).decode()
    cursor.execute("DELETE FROM usuarios WHERE usuario = ?", (u['usuario'],))
    cursor.execute("INSERT INTO usuarios (nombre, apellido, usuario, contraseña, rol) VALUES (?, ?, ?, ?, ?)",
                   (u['nombre'], u['apellido'], u['usuario'], hashed, u['rol']))
conn.commit()
conn.close()
print('Usuarios restablecidos correctamente.')
