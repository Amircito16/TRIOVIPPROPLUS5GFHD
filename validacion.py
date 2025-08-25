#holis esta es mi pequeña parte
import sqlite3

def creartabla():
    baseDeDatos = sqlite3.connect("adivinar.db")
    cr = baseDeDatos.cursor()

    # Creamos la tabla
    cr.execute('''
        CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            descripcion TEXT NOT NULL
        )
    ''')

    # Guardamos los cambios y cerramos la conexión
    baseDeDatos.commit()
    baseDeDatos.close()

def ingresarpalabra(palabra, descripcion):
    # Insertamos una nueva palabra
    baseDeDatos = sqlite3.connect("adivinar.db")
    cr = baseDeDatos.cursor()
    cr.execute('''
        INSERT INTO palabras (palabra, descripcion)
        VALUES (?, ?)
    ''', (palabra, descripcion))
    baseDeDatos.commit()
    baseDeDatos.close()

def palabrarandom():
    # Obtenemos una palabra randomm
    baseDeDatos = sqlite3.connect("adivinar.db")
    cursor = baseDeDatos.cursor()
    cursor.execute('SELECT palabra, descripcion FROM palabras ORDER BY RANDOM() LIMIT 1')
    palabra = cursor.fetchone()
    baseDeDatos.close()
    return palabra
