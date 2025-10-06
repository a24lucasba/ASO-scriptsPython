#!/usr/bin/env python3

from subprocess import run
run("clear", shell=True)


# 13.- Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

inicio = int(input("Introduce el número de inicio: "))
fin = int(input("Introduce el número de fin: "))

for num in range(inicio, fin + 1):
    if num % 2 != 0:
        continue
    print(num)