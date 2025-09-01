from customtkinter import*
#yohana perez

app = CTk()
app.title ("Adivina la palabra")

caja1 =CTkEntry(app,width=150, height=100, font=("Arial",20),justify="right")
caja2 =CTkEntry(app,width=150, height=40, font=("Arial",20),justify="right")

titulo=CTkLabel(app, text="Adivina la palabra",font=("Arial",20))
titulo.grid(column=0,row=0, padx=3, pady=3, columnspan= 5)
genp=CTkButton(app, text="Generar palabra")
genp.grid(column=1,row=1, padx=3, pady=3)
agp=CTkButton(app, text="Agregar palabra")
agp.grid(column=0,row=1, padx=3, pady=3)
verificar=CTkButton(app, text="Verificar")
verificar.grid(column=0,row=5,columnspan= 5, padx=3, pady=3)
caja1.grid(column=0, row=2, columnspan= 5, padx=5,pady=10,sticky="WE")
caja2.grid(column=0, row=3, columnspan= 5, padx=5,pady=10,sticky="WE")

def abrir_agregar_p():
    ven2 =CTkToplevel(app)
    ven2.geometry("300x250")
    titulo2=CTkLabel(ven2, text="Agregar palabra",font=("Arial",20))
    titulo2.grid(column=0, row=0, padx=3, pady=3, columnspan=5)

    palabra_label = CTkLabel(ven2, text="Palabra:", font=("Arial", 14))
    palabra_label.grid(column=0,row=2, padx=3, pady=3,columnspan= 5,sticky="WE")

    entrada_palabra =CTkEntry(ven2, fg_color="white")
    entrada_palabra.grid(column=0,row=3, padx=3, pady=3,columnspan= 5,sticky="WE")

    descripcion_label =CTkLabel(ven2, text="Descripción:", font=("Arial", 14))
    descripcion_label.grid(column=0,row=4, padx=3, pady=3,columnspan= 5,sticky="WE")

    entrada_descripcion =CTkEntry(ven2, fg_color="white")
    entrada_descripcion.grid(column=0,row=5, padx=3, pady=3,columnspan= 5,sticky="WE")

    aceptar=CTkButton(ven2, text="Aceptar")
    aceptar.grid(column=0,row=6, padx=3, pady=3)

    cancelar=CTkButton(ven2, text="Cancelar")
    cancelar.grid(column=1, row=6, padx=3, pady=3)
# para crear el boton agregar y abrir la opcion
boton_agregar =CTkButton(app, text="Agregar palabra",command=abrir_agregar_p)
boton_agregar.grid(column=0,row=1, padx=3, pady=3)




app.resizable(width=False, height=False)

app.mainloop()