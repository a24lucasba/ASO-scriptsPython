#!usr/bin/python3

# 7.- Crea una aplicación que permita adivinar un número generado aleatoriamente entre el 1 y el 100. 
# El programa va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. 
# El programa termina cuando se acierta el número.

from random import randint
from subprocess import run

run("clear", shell=True)

try:

    # Generamos numero aleatorio entre 1 y 100
    numeroOculto = randint(1, 100)

    # Inicializamos contador de intentos
    contador = 0

    while True:

        # Incrementamos el contador de intentos
        contador += 1
        
        # Pedimos al usuario que introduzca un número
        numeroUsuario = int(input("Adivina el número entre 1 y 100: "))

        # Comprobamos si el número es mayor, menor o igual al número oculto
        if numeroUsuario > numeroOculto:
            print("El número es menor")
        elif numeroUsuario < numeroOculto:
            print("El número es mayor")
        else:
            print("¡Has acertado!")
            print (f"Has necesitado {contador} intentos")
            break
except:
    print("Error: Debe ingresar un número válido.")