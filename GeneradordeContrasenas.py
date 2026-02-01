import random

def generarContrasena(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

if __name__ == "__main__":
    longitud_contrasena = int(input("Ingresa la longitud de la contraseña que deseas generar: "))
    contrasena_generada = generarContrasena(longitud_contrasena)
    print("Contraseña generada:", contrasena_generada)