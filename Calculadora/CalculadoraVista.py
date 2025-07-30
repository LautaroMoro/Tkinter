from tkinter import *
from Calculadora import calcular

class CalculadoraVista():
    def __init__(self, ventana):
        self.ventana = ventana
        self.e_texto = Entry(ventana, font=("Calibri 20"))
        self.e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        self.boton1 = Button(ventana, text="1", width=5, height=5, command=lambda: click_boton(1))
        self.boton2 = Button(ventana, text="2", width=5, height=5, command=lambda: click_boton(2))
        self.boton3 = Button(ventana, text="3", width=5, height=5, command=lambda: click_boton(3))
        self.boton4 = Button(ventana, text="4", width=5, height=5, command=lambda: click_boton(4))
        self.boton5 = Button(ventana, text="5", width=5, height=5, command=lambda: click_boton(5))
        self.boton6 = Button(ventana, text="6", width=5, height=5, command=lambda: click_boton(6))
        self.boton7 = Button(ventana, text="7", width=5, height=5, command=lambda: click_boton(7))
        self.boton8 = Button(ventana, text="8", width=5, height=5, command=lambda: click_boton(8))
        self.boton9 = Button(ventana, text="9", width=5, height=5, command=lambda: click_boton(9))
        self.boton0 = Button(ventana, text="0", width=13, height=5, command=lambda: click_boton(0))

        self.boton_sumar = Button(ventana, text="+", width=5, height=5, command=lambda: click_boton("+"))
        self.boton_dividir = Button(ventana, text="/", width=5, height=5, command=lambda: click_boton("/"))
        self.boton_restar = Button(ventana, text="-", width=5, height=5, command=lambda: click_boton("-"))
        self.boton_multiplicar = Button(ventana, text="x", width=5, height=5, command=lambda: click_boton("*"))

        self.boton_igual = Button(ventana, text="=", width=5, height=5, command=lambda: self.evaluar())
        self.boton_decimal = Button(ventana, text=".", width=5, height=5, command=lambda: click_boton("."))
        self.boton_borrar = Button(ventana, text="AC", width=5, height=5,command=lambda: self.borrar())
        self.boton_parentesis1 = Button(ventana, text="(", width=5, height=5, command=lambda: click_boton("("))
        self.boton_parentesis2 = Button(ventana, text=")", width=5, height=5, command=lambda: click_boton(")"))

        self.boton_igual.grid(row=5, column=3, padx=5, pady=5)
        self.boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        self.boton_decimal.grid(row=5, column=2, padx=5, pady=5)

        self.boton1.grid(row=4, column=0, padx=5, pady=5)
        self.boton2.grid(row=4, column=1, padx=5, pady=5)
        self.boton3.grid(row=4, column=2, padx=5, pady=5)
        self.boton_sumar.grid(row=4, column=3, padx=5, pady=5)

        self.boton4.grid(row=3, column=0, padx=5, pady=5)
        self.boton5.grid(row=3, column=1, padx=5, pady=5)
        self.boton6.grid(row=3, column=2, padx=5, pady=5)
        self.boton_restar.grid(row=3, column=3, padx=5, pady=5)

        self.boton7.grid(row=2, column=0, padx=5, pady=5)
        self.boton8.grid(row=2, column=1, padx=5, pady=5)
        self.boton9.grid(row=2, column=2, padx=5, pady=5)
        self.boton_multiplicar.grid(row=2, column=3, padx=5, pady=5)

        self.boton_dividir.grid(row=1, column=3, padx=5, pady=5)
        self.boton_borrar.grid(row=1, column=0, padx=5, pady=5)
        self.boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
        self.boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)

        def click_boton(valor):
            texto_actual = self.e_texto.get()
            self.e_texto.delete(0, END)
            self.e_texto.insert(0, str(texto_actual) + str(valor))
    def borrar(self):
        self.e_texto.delete(0, END)
    def evaluar(self):
        expresion = self.e_texto.get()

        try:
            # Buscar la operación
            for op in ["+", "-", "*", "/"]:
                if op in expresion:
                    partes = expresion.split(op)
                    if len(partes) != 2:
                        raise ValueError("Formato inválido")
                    a = float(partes[0].strip())
                    b = float(partes[1].strip())
                    resultado = calcular(op, a, b)
                    self.e_texto.delete(0, END)
                    self.e_texto.insert(0, str(resultado))
                    return

            raise ValueError("Operación no reconocida")

        except Exception as e:
            self.e_texto.delete(0, END)
            self.e_texto.insert(0, "Error")
            print(f"Error al evaluar la expresión: {e}")