#!/usr/bin/python3

def saludo(nombre=''):
    salida = f"hola {nombre}"

    return salida


n = input("Dime tu nombre: ")
print (saludo(n))