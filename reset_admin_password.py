import sqlite3
import bcrypt

NUEVA_PASS = 'Adm1n#2025!'
DB = 'database.db'

conn = sqlite3.connect(DB)
cursor = conn.cursor()
hashed = bcrypt.hashpw(NUEVA_PASS.encode(), bcrypt.gensalt()).decode()
cursor.execute("UPDATE usuarios SET contraseña = ? WHERE usuario = 'admin'", (hashed,))
conn.commit()
conn.close()
print('Contraseña del admin actualizada correctamente.')
