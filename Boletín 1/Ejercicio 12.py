#!/usr/bin/python3

from subprocess import run
run("clear", shell=True)

# 12.- Crea una aplicación que pida un número y calcule su factorial.

n = int(input("Introduce un número para calcular su factorial: "))
factorial = 1

for i in range(1,n+1):
    factorial = factorial * i

print(f"El factorial de {n} es {factorial}")