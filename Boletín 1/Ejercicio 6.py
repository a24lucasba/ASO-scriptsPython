#!/usr/bin/python3

# Script que pida números hasta que se introduzca un cero.
# esos números se irán metiendo en una lista...
# con la lista ya completa, se debe imprimir la suma de los numeros de la lista y su media
# media = suma de la lista / número de elementos de la lista

#Creamos una lista vacía
lista = []

try:
    while True:
        numero = int(input("Introduce un número (0 para terminar): "))
        if numero != 0:
            lista.append(numero)
        else:
            break
    suma = (sum(lista))  #Suma de los números de la lista
    media = suma / len(lista) if len(lista) > 0 else 0  #Media de los números de la lista

    print(f"Números introducidos: {lista}")
    print(f"Suma de los números: {suma}")
    print(f"Media de los números: {media}")
except:
    print("Error: Debes introducir un número entero")

