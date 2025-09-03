from customtkinter import *
from tkinter import messagebox
from validacion import nuevaPalabra, verificarPalabra, agregarPalabraLogica
from parde_peter import crearTabla, agregarPalabraInicial, cerrarBaseDeDatos

crearTabla()
agregarPalabraInicial()

app = CTk()
app.title("Adivina la palabra")

titulo = CTkLabel(app, text="Adivina la palabra", font=("ArialBlack", 20), text_color="white")
titulo.grid(column=0, row=0, padx=3, pady=3, columnspan=5)

caja_palabra = CTkEntry(app, width=150, height=40, font=("Arial", 20), justify="right", fg_color="lightblue")
caja_palabra.grid(column=0, row=2, columnspan=5, padx=5, pady=10, sticky="WE")

caja_descripcion = CTkEntry(app, width=150, height=40, font=("Arial", 20), justify="right", fg_color="lightblue", state="readonly")
caja_descripcion.grid(column=0, row=3, columnspan=5, padx=5, pady=10, sticky="WE")

label_intentos = CTkLabel(app, text="Intentos restantes: 5", font=("Arial", 14), text_color="white")
label_intentos.grid(column=0, row=4, columnspan=5)

def generar_palabra():
    global palabra_actual, descripcion_actual, intentos_restantes
    p, d, i = nuevaPalabra()
    if p:
        palabra_actual = p
        descripcion_actual = d
        intentos_restantes = i
        caja_palabra.delete(0, END)
        caja_descripcion.configure(state="normal")
        caja_descripcion.delete(0, END)
        caja_descripcion.insert(0, descripcion_actual)
        caja_descripcion.configure(state="readonly")
        label_intentos.configure(text=f"Intentos restantes: {intentos_restantes}")
    else:
        messagebox.showwarning("Error", "No hay palabras en la base de datos.")

def verificar():
    global intentos_restantes
    texto = caja_palabra.get()
    correcto, mensaje = verificarPalabra(texto)
    if correcto:
        messagebox.showinfo("¡Ganaste!", mensaje)
        generar_palabra()
    else:
        if intentos_restantes == 0:
            messagebox.showinfo("Perdiste", mensaje)
            generar_palabra()
        else:
            label_intentos.configure(text=f"Intentos restantes: {intentos_restantes}")
            messagebox.showwarning("Error", mensaje)

def abrir_agregar_palabra():
    ven2 = CTkToplevel(app)
    ven2.geometry("300x250")
    ven2.title("Agregar palabra")

    titulo2 = CTkLabel(ven2, text="Agregar palabra", font=("ArialBlack", 20), text_color="white")
    titulo2.grid(column=0, row=0, padx=3, pady=3, columnspan=5)

    etiqueta_palabra = CTkLabel(ven2, text="Palabra:", font=("Arial", 14))
    etiqueta_palabra.grid(column=0, row=1, padx=3, pady=3, columnspan=5, sticky="WE")

    entrada_palabra = CTkEntry(ven2, fg_color="lightblue", text_color="black")
    entrada_palabra.grid(column=0, row=2, padx=3, pady=3, columnspan=5, sticky="WE")

    etiqueta_descripcion = CTkLabel(ven2, text="Descripción:", font=("Arial", 14))
    etiqueta_descripcion.grid(column=0, row=3, padx=3, pady=3, columnspan=5, sticky="WE")

    entrada_descripcion = CTkEntry(ven2, fg_color="lightblue", text_color="black")
    entrada_descripcion.grid(column=0, row=4, padx=3, pady=3, columnspan=5, sticky="WE")

    def aceptar():
        palabra = entrada_palabra.get()
        descripcion = entrada_descripcion.get()
        ok, msj = agregarPalabraLogica(palabra, descripcion)
        if ok:
            messagebox.showinfo("Éxito", msj)
            ven2.destroy()
        else:
            messagebox.showwarning("Error", msj)

    boton_aceptar = CTkButton(ven2, text="Aceptar", command=aceptar, fg_color="lightgreen", text_color="black")
    boton_aceptar.grid(column=0, row=5, padx=3, pady=3)

    boton_cancelar = CTkButton(ven2, text="Cancelar", command=ven2.destroy, fg_color="lightgreen", text_color="black")
    boton_cancelar.grid(column=1, row=5, padx=3, pady=3)

boton_generar = CTkButton(app, text="Generar palabra", command=generar_palabra, fg_color="lightgreen", text_color="black")
boton_generar.grid(column=1, row=1, padx=3, pady=3)

boton_agregar = CTkButton(app, text="Agregar palabra", command=abrir_agregar_palabra, fg_color="lightgreen", text_color="black")
boton_agregar.grid(column=0, row=1, padx=3, pady=3)

boton_verificar = CTkButton(app, text="Verificar", command=verificar, fg_color="lightgreen", text_color="black")
boton_verificar.grid(column=0, row=5, columnspan=5, padx=3, pady=3)

app.resizable(width=False, height=False)
generar_palabra()
app.mainloop()

cerrarBaseDeDatos()
