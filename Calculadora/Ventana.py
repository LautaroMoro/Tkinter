from tkinter import *
from CalculadoraVista import CalculadoraVista
class Ventana():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Proyecto calculadora")
        self.ventana.geometry("400x400")
        self.msj_label = Label(self.ventana, text="Bienvenido a la Calculadora", background="green")
        self.boton_calculadora = Button(self.ventana, text="Usar calculadora", command=self.abrir_calculadora)
        self.msj_label.grid(row=0, column=1)
        self.boton_calculadora.grid(row=1, column=1)
        self.ventana.mainloop() 

    def abrir_calculadora(self):
        self.ventana.destroy()
        ventana_calculadora = Tk()
        calculadora = CalculadoraVista(ventana_calculadora)
        calculadora.title("Calculadora")
        Label(calculadora.ventana, text="Pantalla con calculadora").pack()

app = Ventana()