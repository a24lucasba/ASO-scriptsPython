#!/usr/bin/env python3

from subprocess import run


# 11.- Programa que muestre un menú donde se proponga realizar las operaciones suma, resta, multiplicación y división de dos números.
# Luego debe devolver el resultado de la operación.

while True:
    run ("clear", shell=True)
    print ("Calculadora básica")
    print ("="*25)
    print ("""Operaciones disponibles:
        suma (+)
        resta (-)
        multiplicación (*)
        división (/)""")
    print ("="*25)







    n1 = float(input("Ingrese el primer número: "))
    op = input("Ingrese la operación a realizar: ")
    n2 = float(input("Ingrese el segundo número: "))
    print ("="*25)


    if op == "+":
        resultado = n1 + n2
        print(f"{n1} {op} {n2} = {resultado}")   
    elif op == "-":
        resultado = n1 - n2
        print(f"{n1} {op} {n2} = {resultado}")  
    elif op == "*":
        resultado = n1 * n2
        print(f"{n1} {op} {n2} = {resultado}")
    elif op == "/":
        if n2 != 0:
            resultado = n1 / n2
            print(f"{n1} {op} {n2} = {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Operación no válida. Por favor, elija entre suma(+), resta(-), multiplicación(*) o división(/).")
    print ("="*25)
    continuar = input("¿Desea realizar otra operación? (s/n): ").lower()
    if continuar != 's':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break