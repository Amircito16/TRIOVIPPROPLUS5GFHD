# parte_pedro.py
from sqlite3 import connect

# Conexión con la base de datos
baseDeDatos = connect("palabras.db")
cr = baseDeDatos.cursor()

# Crear tabla "palabras" si no existe
def crearTabla():
    cr.execute('''
        CREATE TABLE IF NOT EXISTS palabras(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            descripcion TEXT NOT NULL
        )
    ''')
    baseDeDatos.commit()
    print("Tabla 'palabras' creada con éxito.")

# Agregar palabra inicial
def agregarPalabraInicial():
    palabra_inicial = "manzana"
    descripcion_inicial = "Es una fruta roja o verde (eva)"
    cr.execute('SELECT * FROM palabras WHERE palabra = ?', (palabra_inicial,))
    if cr.fetchone() is None:
        cr.execute('INSERT INTO palabras (palabra, descripcion) VALUES (?, ?)', (palabra_inicial, descripcion_inicial))
        baseDeDatos.commit()
        print("Palabra inicial 'manzana' agregada.")
    else:
        print("La palabra 'manzana' ya existe en la base de datos.")

# Funciones para manipular base de datos
def agregarPalabra(nuevaPalabra, nuevaDescripcion):
    cr.execute('INSERT INTO palabras (palabra, descripcion) VALUES (?, ?)', (nuevaPalabra, nuevaDescripcion))
    baseDeDatos.commit()

def verPalabras():
    cr.execute('SELECT * FROM palabras')
    return cr.fetchall()

def seleccionarPalabra():
    cr.execute('SELECT id, palabra, descripcion FROM palabras ORDER BY RANDOM() LIMIT 1')
    return cr.fetchone()

def cerrarBaseDeDatos():
    baseDeDatos.close()

if __name__ == "__main__":
    crearTabla()
    agregarPalabraInicial()
    print("Palabras en la base:")
    for p in verPalabras():
        print(p)
    cerrarBaseDeDatos()
