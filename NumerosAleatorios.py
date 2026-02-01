#Primero importamos la librería random para generar números aleatorios
import random

#Solicitamos al usuario la cantidad de números aleatorios a generar y el rango
numeros_a_generar = int(input("¿Cuántos números aleatorios deseas generar? "))
rango_minimo = int(input("Ingresa el valor mínimo del rango: "))
rango_maximo = int(input("Ingresa el valor máximo del rango: "))

#Esta función genera una lista de números aleatorios dentro del rango especificado
def generar_numeros_aleatorios(cantidad, minimo, maximo):
    numeros = []
    for _ in range(cantidad):
        numero = random.randint(minimo, maximo)
        numeros.append(numero)
    return numeros

#El bloque principal del programa
if __name__ == "__main__":
    numeros_generados = generar_numeros_aleatorios(numeros_a_generar, rango_minimo, rango_maximo)
    print("Números aleatorios generados:")
    for numero in numeros_generados:
        print(numero)