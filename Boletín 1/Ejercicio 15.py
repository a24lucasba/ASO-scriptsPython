#!/usr/bin/env python3

from subprocess import run
run("clear", shell=True)

from math import sqrt

# 15.- Escribe un programa que diga si un número introducido por teclado es o no primo. 
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 

#Declaramos la variable booleana
#Por defecto suponemos que el número es primo
esPrimo = True

n = int(input("Introduce un número entero positivo: "))

for i in range(2, int(sqrt(n)) + 1):
    resto = n % i
    if resto == 0:
        esPrimo = False
        break

print(esPrimo)