
-- Tabla de usuarios
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    usuario TEXT UNIQUE NOT NULL,
    contraseña TEXT NOT NULL,
    rol TEXT NOT NULL CHECK(rol IN ('admin', 'usuario'))
);

-- Tabla de resultados
CREATE TABLE resultados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    bloque TEXT NOT NULL,
    resultado INTEGER NOT NULL,
    cambios_tabs INTEGER NOT NULL,
    reintento INTEGER NOT NULL,
    fecha TEXT NOT NULL
);

-- Tabla de preguntas
CREATE TABLE preguntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bloque TEXT NOT NULL,
    complejidad TEXT NOT NULL,
    pregunta TEXT NOT NULL,
    opciones TEXT NOT NULL,
    respuesta_correcta TEXT NOT NULL
);
