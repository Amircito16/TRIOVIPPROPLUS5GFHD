# parte_amir.py
from tkinter import messagebox, Tk, Frame, Button, Label, Entry, Text, Toplevel
from tkinter import ttk
from sqlite3 import connect

baseDeDatos = connect("palabras.db")
cr = baseDeDatos.cursor()

intentos_restantes = 5
palabra_actual = ""
descripcion_actual = ""
longitud_palabra = 0

def seleccionarPalabra():
    cr.execute('SELECT id, palabra, descripcion FROM palabras ORDER BY RANDOM() LIMIT 1')
    return cr.fetchone()

def nuevaPalabra():
    global intentos_restantes, palabra_actual, descripcion_actual, longitud_palabra
    palabra = seleccionarPalabra()
    if palabra:
        palabra_actual = palabra[1]
        descripcion_actual = palabra[2]
        longitud_palabra = len(palabra_actual)
        intentos_restantes = 5
        info_label.config(text=f"Descripción: {descripcion_actual}")
        longitud_label.config(text=f"Longitud: {longitud_palabra}")
        intentos_label.config(text=f"Intentos restantes: {intentos_restantes}")
        palabra_entry.delete(0, "end")
    else:
        messagebox.showwarning("Base vacía", "No hay palabras en la base de datos.")

def verificarPalabra():
    global intentos_restantes
    palabra_usuario = palabra_entry.get()
    if palabra_usuario.lower() == palabra_actual.lower():
        messagebox.showinfo("¡Ganaste!", "¡Felicidades, adivinaste la palabra!")
        nuevaPalabra()
    else:
        intentos_restantes -= 1
        if intentos_restantes == 0:
            messagebox.showinfo("Perdiste", f"¡Perdiste! La palabra era: {palabra_actual}")
            nuevaPalabra()
        else:
            intentos_label.config(text=f"Intentos restantes: {intentos_restantes}")
            messagebox.showwarning("Intenta de nuevo", "La palabra es incorrecta. Sigue intentándolo.")

def agregarPalabra():
    if nombrePalabra.get() == "" or descripcion.get("1.0", "end") == "\n":
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        return
    nuevaPalabraTexto = str(nombrePalabra.get())
    nuevaDescripcion = descripcion.get("1.0", "end").strip()
    cr.execute('INSERT INTO palabras (palabra, descripcion) VALUES (?, ?)', (nuevaPalabraTexto, nuevaDescripcion))
    baseDeDatos.commit()
    messagebox.showinfo("Acción exitosa", "La palabra fue agregada con éxito")

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

app = Tk()
app.title("Adivina la Palabra")

frame_acciones = Frame(app)
frame_acciones.grid(row=0, column=0, padx=10, pady=10)
btn_nueva_palabra = Button(frame_acciones, text="Nueva Palabra", command=nuevaPalabra)
btn_nueva_palabra.grid(row=0, column=0, padx=5, pady=5)

frame_info = Frame(app)
frame_info.grid(row=0, column=1, padx=10, pady=10)
info_label = Label(frame_info, text="Descripción: ")
info_label.grid(row=0, column=0, sticky="wens", columnspan=2)
longitud_label = Label(frame_info, text="Longitud: ")
longitud_label.grid(row=1, column=0, sticky="wens", columnspan=2)
intentos_label = Label(frame_info, text="Intentos restantes: ")
intentos_label.grid(row=2, column=0, sticky="wens", columnspan=2)

frame_jugar = Frame(app)
frame_jugar.grid(row=1, column=0, padx=10, pady=10)
palabra_entry = Entry(frame_jugar)
palabra_entry.grid(row=0, column=0, padx=5, pady=5)
btn_comprobar = Button(frame_jugar, text="Comprobar", command=verificarPalabra)
btn_comprobar.grid(row=1, column=0, padx=5, pady=5)

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

resultado = Label(app, text="La palabra es: ")
resultad2 = Label(app, text="La descripcion es: ")
resultado.grid(row=5, column=0, columnspan=3)
resultad2.grid(row=6, column=0, columnspan=3)

btn_agregar = Button(app, text="Agregar", command=agregarPalabra)
btn_agregar.grid(row=7, column=0)

btn_ver = Button(app, text="Ver Palabras", command=verPalabras)
btn_ver.grid(row=7, column=1)

btn_cerrar = Button(app, text='Cerrar', command=app.quit)
btn_cerrar.grid(row=7, column=2)

nuevaPalabra()
app.mainloop()

baseDeDatos.close()
