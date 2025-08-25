from customtkinter import*

#yohana perez

app = CTk()
app.title ("Adivina la palabra")
ventana_inicial = CTkFrame(app)
ventana_inicial.grid(column=0,row=0,padx=3, pady=3)

titulo=CTkLabel(ventana_inicial, text="BIENVENIDO",font=("Arial",20))
titulo.grid(column=0,row=0, padx=3, pady=3)
jugar=CTkButton(ventana_inicial, text="JUGAR")
jugar.grid(column=0,row=1, padx=3, pady=3)
salir=CTkButton(ventana_inicial, text="SALIR")
salir.grid(column=0,row=2, padx=3, pady=3)

app.resizable(width=False, height=False)


app.mainloop()