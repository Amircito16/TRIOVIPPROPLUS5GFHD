#PEDRO LOPEZ; Esta es mi parte bros!!!
#YOHANA PEREZ
#ASAHEL LOPEZ
#5TO. ELECTRONICA
#PROYECTO: "ADIVINA LA PALABRA"

from sqlite3 import *

#CONEXION CON LA BASE DE DATOS
baseDeDatos = connect("palabra.db")
cr = baseDeDatos.cursor()

#FUNCION PARA AGREGAR UNA PALABRA INICIAL
def agregarPalabraInicial():
    palabra_inicial = "manzana"
    descripcion_inicial = "Es una fruta roja o verde (eva)"

    #VERIFICA SI LA PALABRA YA EXISTE EN LA BASE DE DATOS
    cr.execute('SELECT * FROM palabras WHERE palabra = ?', (palabra_inicial,))
    if cr.fetchone() is None: #SOLO AGREGA SI LA PALABRA NO EXISTE
        cr.execute('INSERT INTO palabras (palabra, descripcion) VALUES (?, ?)', (palabra_inicial, descripcion_inicial))
        baseDeDatos.commit()
        print("Plabara inicial 'manzana' agregada")
    else:
        print("La palabra 'manzana' ya existe en la base de datos")

#LLAMAR ALA FUNCION PARA ASEGURARNOA DE QUE LA PALABRA 'manzana' ESTA EN LA BASE DE DATOS
agregarPalabraInicial()

#CREAR TABLA
def crearTabla():
    cr.execute('''
        CREATE TABLE IF NOT EXISTS adivina(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            descripcion TEXT NOT NULL);''')
    baseDeDatos.commit()
    print("Tabla creada con éxito ")

#FUNCION PARA AGREGAR UNA NUEVA PALABRA
def agregarPalabra(nuevaPalabra, nuevaDescripcion):
    cr.execute('''
        INSERT INTO palabras (palabra, descripcion)
        VALUES (?, ?)''', (nuevaPalabra, nuevaDescripcion))
    baseDeDatos.commit()

#FUNCION PARA VER TODAS LAS PALABRA
def verPalabras():
    cr.execute('SELECT * FROM palabras')
    return cr.fetchall()

#FUNCION PARA SELECCIONAR UNA PALABRA ALEATORIA
def seleccionarPalabra():
    cr.execute('SELECT id, palabra, descripcion FROM palabras ORDER BY RANDOM() LIMIT 1')
    return cr.fetchone()

#FUNCION PARA CERRAR LA BASE DE DATO
def cerrarBaseDeDatos():
    baseDeDatos.close()

baseDeDatos.commit()