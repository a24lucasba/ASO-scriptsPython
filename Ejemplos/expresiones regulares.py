#!/var/bin/python3

from re import search,compile

texto = input("Ingrese texto: ")

stringPatronSimbol = '\W'
patronSimbol =compile(stringPatronSimbol)

if patronSimbol.search(texto):
    print("El texto contiene simbolos")
else:
    print("El texto no contiene simbolos")
