import sqlite3

baseDeDatos = sqlite3.connect("palabras.db")
cr = baseDeDatos.cursor()

def crearTabla():
    cr.execute('''
        CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            descripcion TEXT NOT NULL
        )
    ''')
    baseDeDatos.commit()

def agregarPalabraInicial():
    palabra_inicial = "manzana"
    descripcion_inicial = "Es una fruta roja o verde"
    cr.execute('SELECT * FROM palabras WHERE palabra = ?', (palabra_inicial,))
    if cr.fetchone() is None:
        cr.execute('INSERT INTO palabras (palabra, descripcion) VALUES (?, ?)', (palabra_inicial, descripcion_inicial))
        baseDeDatos.commit()

def agregarPalabra(palabra, descripcion):
    cr.execute('INSERT INTO palabras (palabra, descripcion) VALUES (?, ?)', (palabra, descripcion))
    baseDeDatos.commit()

def verPalabras():
    cr.execute('SELECT * FROM palabras')
    return cr.fetchall()

def seleccionarPalabra():
    cr.execute('SELECT id, palabra, descripcion FROM palabras ORDER BY RANDOM() LIMIT 1')
    return cr.fetchone()

def cerrarBaseDeDatos():
    baseDeDatos.close()
