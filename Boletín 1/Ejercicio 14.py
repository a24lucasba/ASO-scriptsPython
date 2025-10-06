#!/usr/bin/env python3

from subprocess import run
run ("clear" , shell=[True])

# 14.- Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. 
# No se puede utilizar el operador de potencia (**) o la función pow .


base = float(input("Introduce la base (número real): "))
sol = base
exponente = int(input("Introduce el exponente (entero positivo): "))


if exponente == 0:
    sol=1
else:
    for i in range(1, exponente):
        sol = base * sol

print(f'{base} elevado a {exponente} es {sol}')