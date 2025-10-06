#!/usr/bin/python3

from subprocess import run
run("clear", shell=True)

# Lista de Fibonacci

lista = [0, 1]
nMax = int(input("Introduce el número máximo de la serie de Fibonacci: "))

while True:
    nuevo = lista[-1]+lista[-2]
    if nuevo > nMax:
        break
    lista.append(nuevo)

salida=(', '.join(lista))
print(salida)