from customtkinter import*
#yohana perez

app = CTk()
app.title ("Adivina la palabra")

caja1 =CTkEntry(app,width=150, height=100, font=("Arial",20),justify="right")
caja2 =CTkEntry(app,width=150, height=40, font=("Arial",20),justify="right")

titulo=CTkLabel(app, text="ADIVINA LA PALABRA",font=("Arial",20))
titulo.grid(column=0,row=0, padx=3, pady=3, columnspan= 5)
genp=CTkButton(app, text="Generar palabra")
genp.grid(column=1,row=1, padx=3, pady=3)
agp=CTkButton(app, text="Agregar palabra")
agp.grid(column=0,row=1, padx=3, pady=3)
verificar=CTkButton(app, text="Verificar")
verificar.grid(column=0,row=5,columnspan= 5, padx=3, pady=3)
caja1.grid(column=0, row=2, columnspan= 5, padx=5,pady=10,sticky="WE")
caja2.grid(column=0, row=3, columnspan= 5, padx=5,pady=10,sticky="WE")





app.resizable(width=True, height=True)

app.mainloop()