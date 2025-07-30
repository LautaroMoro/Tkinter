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