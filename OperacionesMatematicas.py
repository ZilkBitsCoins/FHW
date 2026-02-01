import math

def operaciones_matematicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    potencia = math.pow(a, b)
    
    return {
        "suma": suma,
        "resta": resta,
        "multiplicacion": multiplicacion,
        "division": division,
        "potencia": potencia
    }

print(operaciones_matematicas(5, 3))
