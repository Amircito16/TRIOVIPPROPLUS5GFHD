#holis esta es mi pequeña parte
import sqlite3



# Funciones de base de datos
def creartabla():
    baseDeDatos = sqlite3.connect("adivinar.db")
    cr = baseDeDatos.cursor()
    cr.execute(''' 
        CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            descripcion TEXT NOT NULL
        )
    ''')
    baseDeDatos.commit()
    baseDeDatos.close()


def ingresarpalabra(palabra, descripcion):
    baseDeDatos = sqlite3.connect("adivinar.db")
    cr = baseDeDatos.cursor()
    cr.execute(''' 
        INSERT INTO palabras (palabra, descripcion) 
        VALUES (?, ?)
    ''', (palabra, descripcion))
    baseDeDatos.commit()
    baseDeDatos.close()


def palabrarandom():
    baseDeDatos = sqlite3.connect("adivinar.db")
    cursor = baseDeDatos.cursor()
    cursor.execute('SELECT palabra, descripcion FROM palabras ORDER BY RANDOM() LIMIT 1')
    palabra = cursor.fetchone()
    baseDeDatos.close()

    if palabra is None:
        return "", ""
    return palabra


