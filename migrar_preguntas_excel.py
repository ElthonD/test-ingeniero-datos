import pandas as pd
import sqlite3

# Leer el archivo Excel
df = pd.read_excel('preguntas.xlsx')

# Conexión a la base de datos
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Crear la tabla si no existe (ajusta los nombres de columnas según tu Excel)
cursor.execute('''
CREATE TABLE IF NOT EXISTS preguntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bloque TEXT NOT NULL,
    complejidad TEXT NOT NULL,
    pregunta TEXT NOT NULL,
    opciones TEXT NOT NULL,
    respuesta_correcta TEXT NOT NULL
)
''')

# Limpiar la tabla antes de migrar (opcional)
cursor.execute('DELETE FROM preguntas')

# Insertar preguntas
for _, row in df.iterrows():
    bloque = str(row['bloque'])
    complejidad = str(row['complejidad'])
    pregunta = str(row['pregunta'])
    # Suponiendo que las opciones están en columnas separadas: opcion_a, opcion_b, opcion_c, opcion_d
    opciones = str([
        row.get('opcion_a', ''),
        row.get('opcion_b', ''),
        row.get('opcion_c', ''),
        row.get('opcion_d', '')
    ])
    respuesta_correcta = str(row['respuesta_correcta'])
    cursor.execute('''
        INSERT INTO preguntas (bloque, complejidad, pregunta, opciones, respuesta_correcta)
        VALUES (?, ?, ?, ?, ?)
    ''', (bloque, complejidad, pregunta, opciones, respuesta_correcta))

conn.commit()
conn.close()

print('Migración completada. Las preguntas han sido insertadas en la base de datos.')
