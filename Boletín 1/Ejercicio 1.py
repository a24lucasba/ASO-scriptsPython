#!usr/bin/python3

# 1.- Hacer un programa que pida el radio por pantalla y devuelva el perímetro, el área y el volumen utilizando dicho parámetro:
# Nota: En la resolución de este problema se utiliza el módulo math.

from math import pi, pow
from subprocess import run


run("clear", shell=True)

try:
    # Pedimos al usuario que introduzca el radio
    radio = float(input("Ingrese el radio: "))

    # Calculamos perímetro, área y volumen
    perimetro = 2 * pi * radio
    area = pi * pow(radio,2)
    volumen = (4/3) * pi * pow(radio,3)

    # Mostramos los resultados
    print(f"El perímetro es: {perimetro}")
    print(f"El área es: {area}")
    print(f"El volumen es: {volumen}")
except:
    print("Error: Debe ingresar un número válido para el radio.")