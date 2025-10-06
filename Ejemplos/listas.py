#!/usr/bin/python3

lista = [1, 2, 3, 4, 5]

print(lista)

lista.append(6)  #Añadir elemento al final de la lista
print(lista)
lista.pop()    #Eliminar el último elemento de la lista
print(lista)
lista.insert(0, 0)  #Añadir elemento al principio de la lista
print(lista)
lista.remove(0)  #Eliminar el primer elemento de la lista
print(lista)

print(lista[0]) #Primer elemento

print(lista[-1]) #Último elemento

print(lista[len(lista)-2])  #Penúltimo elemento

print(f"Tamaño de la lista: {len(lista)}")  #Tamaño de la lista
