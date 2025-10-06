#!/usr/bin/env python3

from subprocess import run
run ("clear", shell=True)


# 9.- Realiza un programa que pida una nota numérica entera e imprima su equivalente en texto: 
#            0-2 => Muy Deficiente, 3-4 => Insuficiente, 5 => Suficiente, 
#            6 => Bien, 7-8 => Notable, 9-10 => Sobresaliente, otro => Error


dNotas = {
    0: "Muy Deficiente", 1: "Muy Deficiente", 2: "Muy Deficiente",
    3: "Insuficiente", 4: "Insuficiente",
    5: "Suficiente",
    6: "Bien",
    7: "Notable", 8: "Notable",
    9: "Sobresaliente", 10: "Sobresaliente"
}
nota = float(input("Introduce una nota numérica entera (0-10): "))
nota = int(nota)
print(dNotas[nota])