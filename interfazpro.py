# main.py

from customtkinter import *
from game_logic import nueva_palabra, verificar_palabra, agregar_palabra_db

app = CTk()
app.title("Adivina la palabra")
app.geometry("500x400")
app.resizable(width=False, height=False)

# ELEMENTOS GLOBALES
caja_palabra = CTkEntry(app, width=150, height=40, font=("Arial", 20), justify="center", fg_color="lightblue")
caja_resultado = CTkLabel(app, text="", font=("Arial", 14), text_color="white")
descripcion_label = CTkLabel(app, text="", font=("Arial", 16), text_color="white")

# FUNCIONES DE BOTONES
def generar_nueva():
    descripcion, longitud, intentos = nueva_palabra()
    descripcion_label.configure(text=f"Descripción: {descripcion}  |  Longitud: {longitud}")
    caja_resultado.configure(text=f"Intentos restantes: {intentos}")
    caja_palabra.delete(0, END)

def verificar():
    palabra_usuario = caja_palabra.get()
    resultado, info = verificar_palabra(palabra_usuario)

    if resultado == "correcto":
        caja_resultado.configure(text=f"✅ ¡Correcto! Era '{info}'. Generando nueva...")
        generar_nueva()
    elif resultado == "fallaste":
        caja_resultado.configure(text=f"❌ Te quedaste sin intentos. La palabra era '{info}'")
        generar_nueva()
    else:
        caja_resultado.configure(text=f"❗ Incorrecto. Intentos restantes: {info}")

def abrir_agregar_p():
    ventana = CTkToplevel(app)
    ventana.geometry("300x250")
    ventana.title("Agregar palabra")

    CTkLabel(ventana, text="Palabra:", font=("Arial", 14)).pack(pady=5)
    entrada_palabra = CTkEntry(ventana, fg_color="lightblue")
    entrada_palabra.pack(pady=5)

    CTkLabel(ventana, text="Descripción:", font=("Arial", 14)).pack(pady=5)
    entrada_descripcion = CTkEntry(ventana, fg_color="lightblue")
    entrada_descripcion.pack(pady=5)

    def aceptar():
        palabra = entrada_palabra.get()
        descripcion = entrada_descripcion.get()
        if agregar_palabra_db(palabra, descripcion):
            ventana.destroy()
        else:
            CTkLabel(ventana, text="⚠️ Completa todos los campos", text_color="red").pack()

    CTkButton(ventana, text="Aceptar", command=aceptar, fg_color="lightgreen", text_color="black").pack(pady=10)
    CTkButton(ventana, text="Cancelar", command=ventana.destroy, fg_color="lightgreen", text_color="black").pack()

# UI PRINCIPAL
titulo = CTkLabel(app, text="Adivina la palabra", font=("ArialBlack", 24), text_color="white")
titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=5)

descripcion_label.grid(column=0, row=1, columnspan=5, padx=10, pady=5)
caja_palabra.grid(column=0, row=2, columnspan=5, padx=10, pady=5)
caja_resultado.grid(column=0, row=3, columnspan=5, padx=10, pady=5)

CTkButton(app, text="Generar palabra", command=generar_nueva, fg_color="lightgreen", text_color="black").grid(column=0, row=4, padx=5, pady=5)
CTkButton(app, text="Verificar", command=verificar, fg_color="lightgreen", text_color="black").grid(column=1, row=4, padx=5, pady=5)
CTkButton(app, text="Agregar palabra", command=abrir_agregar_p, fg_color="lightgreen", text_color="black").grid(column=2, row=4, padx=5, pady=5)

# Iniciar con una palabra
generar_nueva()
app.mainloop()
