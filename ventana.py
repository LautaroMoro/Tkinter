import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x400")

#etiqueta = tkinter.Label(ventana, text = "Hola mundo", backg = "red")
#etiqueta.pack(fill = tkinter.BOTH, expand = True)

#def saludo(nombre):
#    print("Hola " + nombre)
#btn1 = tkinter.Button(ventana, text = "Presiona", padx=30, pady=20, command= lambda: saludo("lauti"))
#btn1.pack()
"""
campoTexto = tkinter.Entry(ventana, font = "Helvetica 14")
campoTexto.pack()
etiqueta = tkinter.Label(ventana)
etiqueta.pack() 
def mostrarTexto():
    texto = campoTexto.get()
    etiqueta["text"] = texto

btn1 = tkinter.Button(ventana, text="Click", command = mostrarTexto)
btn1.pack()
"""
btn1 = tkinter.Button(ventana, text = "boton1")
btn2 = tkinter.Button(ventana, text = "boton2")

btn1.grid(row = 0, column=0)
btn2.grid(row = 1, column=1)
ventana.mainloop()