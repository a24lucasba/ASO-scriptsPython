#!usr/bin/python3

# 1.- Hacer un programa que pida el radio por pantalla y devuelva el perímetro, el área y el volumen utilizando dicho parámetro:
# Nota: En la resolución de este problema se utiliza el módulo math.

from math import pi, pow
from subprocess import run
import sys


run("clear", shell=True)

def perimetro(radio=''):
    calc = 2 * pi * radio
    salida = (f'El perímetro es de {calc} cm')
    return salida
def area(radio=''):
    calc = pi * pow(radio,2)
    salida = (f'El área es de {calc} cm²')
    return salida
def volumen(radio=''):
    calc = (4/3) * pi * pow(radio,3)
    salida = (f'El volumen es de {calc} cm³')
    return salida

try:
    r = float(input("Ingresa el radio en cm: "))
    print ("-"*30)
    print (perimetro(r))
    print ("-"*30)
    print (area(r))
    print ("-"*30)
    print (volumen(r))
    print ("-"*30)

except:
    print("Error: Debe ingresar un número válido para el radio.")