# database.py
from sqlite3 import connect

# Conexión a la base de datos
baseDeDatos = connect("palabras.db")
cr = baseDeDatos.cursor()

# Crear la tabla si no existe
def crearTabla():
    cr.execute('''
        CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            descripcion TEXT NOT NULL
        );
    ''')
    baseDeDatos.commit()

# Agregar una nueva palabra
def agregarPalabra(palabra, descripcion):
    cr.execute('''
        INSERT INTO palabras (palabra, descripcion)
        VALUES (?, ?)
    ''', (palabra, descripcion))
    baseDeDatos.commit()

# Obtener todas las palabras
def verPalabras():
    cr.execute('SELECT * FROM palabras')
    return cr.fetchall()

# Obtener palabra aleatoria
def seleccionarPalabra():
    cr.execute('SELECT id, palabra, descripcion FROM palabras ORDER BY RANDOM() LIMIT 1')
    return cr.fetchone()

# Cerrar conexión (si se necesita)
def cerrarBaseDeDatos():
    baseDeDatos.close()
