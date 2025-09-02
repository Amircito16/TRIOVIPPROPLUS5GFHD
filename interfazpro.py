# parte_yohana.py
from customtkinter import CTk, CTkEntry, CTkLabel, CTkButton, CTkToplevel

app = CTk()
app.title("Adivina la palabra")

caja1 = CTkEntry(app, width=150, height=100, font=("Arial", 20), justify="right", fg_color="lightblue")
caja2 = CTkEntry(app, width=150, height=40, font=("Arial", 20), justify="right", fg_color="lightblue")

titulo = CTkLabel(app, text="Adivina la palabra", font=("ArialBlack", 20), text_color="white")
titulo.grid(column=0, row=0, padx=3, pady=3, columnspan=5)

genp = CTkButton(app, text="Generar palabra", fg_color="lightgreen", text_color="black")
genp.grid(column=1, row=1, padx=3, pady=3)

agp = CTkButton(app, text="Agregar palabra", fg_color="lightgreen", text_color="black")
agp.grid(column=0, row=1, padx=3, pady=3)

verificar = CTkButton(app, text="Verificar", fg_color="lightgreen", text_color="black")
verificar.grid(column=0, row=5, columnspan=5, padx=3, pady=3)

caja1.grid(column=0, row=2, columnspan=5, padx=5, pady=10, sticky="WE")
caja2.grid(column=0, row=3, columnspan=5, padx=5, pady=10, sticky="WE")

def abrir_agregar_p():
    ven2 = CTkToplevel(app)
    ven2.geometry("300x250")
    titulo2 = CTkLabel(ven2, text="Agregar palabra", font=("ArialBlack", 20), text_color="white")
    titulo2.grid(column=0, row=0, padx=3, pady=3, columnspan=5)

    palabra = CTkLabel(ven2, text="Palabra:", font=("Arial", 14))
    palabra.grid(column=0, row=2, padx=3, pady=3, columnspan=5, sticky="WE")

    palabrae = CTkEntry(ven2, fg_color="lightblue", text_color="black")
    palabrae.grid(column=0, row=3, padx=3, pady=3, columnspan=5, sticky="WE")

    descripcion = CTkLabel(ven2, text="Descripción:", font=("Arial", 14))
    descripcion.grid(column=0, row=4, padx=3, pady=3, columnspan=5, sticky="WE")

    descripcione = CTkEntry(ven2, fg_color="lightblue", text_color="black")
    descripcione.grid(column=0, row=5, padx=3, pady=3, columnspan=5, sticky="WE")

    aceptar = CTkButton(ven2, text="Aceptar", text_color="black", fg_color="lightgreen")
    aceptar.grid(column=0, row=6, padx=3, pady=3)

    cancelar = CTkButton(ven2, text="Cancelar", text_color="black", fg_color="lightgreen")
    cancelar.grid(column=1, row=6, padx=3, pady=3)

boton_agregar = CTkButton(app, text="Agregar palabra", command=abrir_agregar_p, text_color="black", fg_color="lightgreen")
boton_agregar.grid(column=0, row=1, padx=3, pady=3)

app.resizable(width=False, height=False)
app.mainloop()
