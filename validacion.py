#holis esta es mi pequeña parte
from tkinter import messagebox, Tk, Frame, Button, Label, Entry, Text
from tkinter import ttk
from sqlite3 import connect
import random

# Conexión y configuración de la base de datos
baseDeDatos = connect("palabras.db")
cr = baseDeDatos.cursor()

# Función para seleccionar una palabra aleatoria de la base de datos
def seleccionarPalabra():
    cr.execute('SELECT id, palabra, descripcion FROM palabras ORDER BY RANDOM() LIMIT 1')
    palabra = cr.fetchone()  # Devuelve una tupla con (id, palabra, descripcion)
    return palabra

# Variables globales del juego
intentos_restantes = 5
palabra_actual = ""
descripcion_actual = ""
longitud_palabra = 0

# Función para iniciar un nuevo juego con una palabra aleatoria
def nuevaPalabra():
    global intentos_restantes, palabra_actual, descripcion_actual, longitud_palabra

    # Seleccionar una palabra aleatoria de la base de datos
    palabra = seleccionarPalabra()
    palabra_actual = palabra[1]
    descripcion_actual = palabra[2]
    longitud_palabra = len(palabra_actual)
    intentos_restantes = 5  # Número de intentos disponibles

    # Actualizar la interfaz gráfica con la nueva descripción y longitud
    info_label.config(text=f"Descripción: {descripcion_actual}")
    longitud_label.config(text=f"Longitud: {longitud_palabra}")
    intentos_label.config(text=f"Intentos restantes: {intentos_restantes}")

# Función para verificar la respuesta del jugador
def verificarPalabra():
    global intentos_restantes

    palabra_usuario = palabra_entry.get()  # Obtenemos la palabra que ingresó el jugador

    if palabra_usuario.lower() == palabra_actual.lower():  # Verifica si la palabra es correcta
        messagebox.showinfo("¡Ganaste!", "¡Felicidades, adivinaste la palabra!")
        nuevaPalabra()  # Iniciar un nuevo juego con una nueva palabra
    else:
        intentos_restantes -= 1  # Restar un intento si la palabra es incorrecta
        if intentos_restantes == 0:
            messagebox.showinfo("Perdiste", f"¡Perdiste! La palabra era: {palabra_actual}")
            nuevaPalabra()  # Iniciar un nuevo juego si se pierden todos los intentos
        else:
            # Actualizar la cantidad de intentos restantes
            intentos_label.config(text=f"Intentos restantes: {intentos_restantes}")
            messagebox.showwarning("Intenta de nuevo", "La palabra es incorrecta. Sigue intentándolo.")

# Función para agregar una nueva palabra a la base de datos
def agregarPalabra():
    if nombrePalabra.get() == "" or descripcion.get("1.0", "end") == "\n":
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        return
    else:
        nuevaPalabraTexto = str(nombrePalabra.get())
        nuevaDescripcion = descripcion.get("1.0", "end").strip()
        cr.execute('''
            INSERT INTO palabras (palabra, descripcion)
            VALUES (?, ?)
        ''', (nuevaPalabraTexto, nuevaDescripcion))
        baseDeDatos.commit()
        messagebox.showinfo("Acción exitosa", "La palabra fue agregada con éxito")

# Función para ver las palabras de la base de datos
def verPalabras():
    def cerrarVentana():
        ventanaTabla.destroy()

    ventanaTabla = Toplevel(app)
    ventanaTabla.title("Palabras registradas")
