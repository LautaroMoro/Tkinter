class Calculadora:
    def __init__(self):
        self.primer_numero = None
        self.segundo_numero = None
        self.operacion = None
        def sumar(a, b):
            return a + b
        def restar(a, b):
            return a - b
        def multiplicar(a, b):
            return a * b
        def dividir(a, b):
            return a / b
        def calcular(operacion, a, b):
            match operacion:
                case "+":
                    return sumar(a, b)
                case "-":
                    return restar(a, b)
                case "*":
                    return multiplicar(a, b)
                case "/":
                    return dividir(a, b)
                case _:
                    raise ValueError("Operación no válida")
    def obtener_primer_numero(self):
        return self.primer_numero
    def obtener_segundo_numero(self):
        return self.segundo_numero
    def obtener_operacion(self):
        return self.operacion
    a = obtener_primer_numero()
    b = obtener_segundo_numero()
    op =obtener_operacion() 