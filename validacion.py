#holis esta es mi pequeña parte
from tkinter import messagebox, Tk, Frame, Button, Label, Entry, Text, Toplevel
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

    tabla = ttk.Treeview(ventanaTabla, columns=("ID", "Palabra", "Descripcion"), show="headings")
    tabla.column("ID", width=20, anchor="center")
    tabla.heading("ID", text="ID")
    tabla.heading("Palabra", text="Palabra")
    tabla.heading("Descripcion", text="Descripción")
    tabla.grid(row=0, column=0, columnspan=3)

    botonCerrar = Button(ventanaTabla, text="Cerrar", command=cerrarVentana)
    botonCerrar.grid(row=1, column=0, padx=10, pady=10)

    cr.execute('SELECT * FROM palabras')
    palabras = cr.fetchall()
    for palabra in palabras:
        tabla.insert("", "end", values=palabra)

# Crear la ventana principal
app = Tk()
app.title("Adivina la Palabra")

# Configuración de la interfaz gráfica
# Apartado de Acciones
acciones_frame = Frame(app)
acciones_frame.grid(row=0, column=0, padx=10, pady=10)
nueva_palabra_btn = Button(acciones_frame, text="Nueva Palabra", command=nuevaPalabra)
nueva_palabra_btn.grid(row=0, column=0, padx=5, pady=5)

# Apartado de Información
informacion_frame = Frame(app)
informacion_frame.grid(row=0, column=1, padx=10, pady=10)
info_label = Label(informacion_frame, text="Descripción: ")
info_label.grid(row=0, column=0, sticky="wens", columnspan=2)

longitud_label = Label(informacion_frame, text="Longitud: ")
longitud_label.grid(row=1, column=0, sticky="wens", columnspan=2)

intentos_label = Label(informacion_frame, text="Intentos restantes: ")
intentos_label.grid(row=2, column=0, sticky="wens", columnspan=2)

# Apartado de Jugar
jugar_frame = Frame(app)
jugar_frame.grid(row=1, column=0, padx=10, pady=10)
palabra_entry = Entry(jugar_frame)
palabra_entry.grid(row=0, column=0, padx=5, pady=5)
comprobar_btn = Button(jugar_frame, text="Comprobar", command=verificarPalabra)
comprobar_btn.grid(row=1, column=0, padx=5, pady=5)

# Apartado de Agregar palabra
etiqueta1 = Label(app, text="Agregue una palabra nueva", font=(25))
etiqueta1.grid(row=2, column=0, sticky="wens", columnspan=4)

etiqueta2 = Label(app, text='Ingrese la palabra: ', fg='blue', font=(20))
etiqueta2.grid(row=3, column=0, sticky='wens', columnspan=2)
nombrePalabra = Entry(app)
nombrePalabra.grid(row=3, column=2, sticky='wens', columnspan=4)

etiqueta3 = Label(app, text='Ingrese la descripcion: ', fg='blue', font=(20))
etiqueta3.grid(row=4, column=0, sticky='wens', columnspan=2)
descripcion = Text(app, height=5, width=30)
descripcion.grid(row=4, column=2, sticky='wens', columnspan=3, pady=5, padx=3)

# Etiquetas de resultado
resultado = Label(app, text="La palabra es: ")
resultad2 = Label(app, text="La descripcion es: ")
resultado.grid(row=5, column=0, columnspan=3)
resultad2.grid(row=6, column=0, columnspan=3)

# Botones de acciones
resul = Button(app, text="Agregar", command=agregarPalabra)
resul.grid(row=7, column=0)

ver = Button(app, text="Ver Palabras", command=verPalabras)
ver.grid(row=7, column=1)

cerrarP = Button(app, text='Cerrar', command=app.quit)
cerrarP.grid(row=7, column=2)

# Iniciar el juego con una nueva palabra
nuevaPalabra()

# Ejecutar la aplicación
app.mainloop()

# Cerrar la base de datos cuando termine el programa
baseDeDatos.close()
