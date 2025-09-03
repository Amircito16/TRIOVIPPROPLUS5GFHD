# game_logic.py

from database import seleccionarPalabra, agregarPalabra, verPalabras

# Variables globales del juego
intentos_restantes = 5
palabra_actual = ""
descripcion_actual = ""

# Iniciar nueva palabra
def nueva_palabra():
    global palabra_actual, descripcion_actual, intentos_restantes
    palabra = seleccionarPalabra()
    palabra_actual = palabra[1]
    descripcion_actual = palabra[2]
    intentos_restantes = 5
    return descripcion_actual, len(palabra_actual), intentos_restantes

# Verificar intento del jugador
def verificar_palabra(palabra_usuario):
    global intentos_restantes

    if palabra_usuario.lower() == palabra_actual.lower():
        return "correcto", palabra_actual
    else:
        intentos_restantes -= 1
        if intentos_restantes == 0:
            return "fallaste", palabra_actual
        else:
            return "intenta", intentos_restantes

# Agregar nueva palabra a la DB
def agregar_palabra_db(palabra, descripcion):
    if palabra.strip() == "" or descripcion.strip() == "":
        return False
    agregarPalabra(palabra, descripcion)
    return True
