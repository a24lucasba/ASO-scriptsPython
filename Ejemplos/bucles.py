#!/usr/bin/python3


## Ejempo 1 - Recorrer una lista

# lNum = [24, 56, 67, 45, 33]
# for n in lNum:
#     print(n, end=' - ')


## Ejempo 2 - Tabla de multiplicar del 5

# i= 5
# for j in range(1, 11):
#     m= i * j
#     print(f"{i} x {j} = {m}")

## Ejemplo 3 - Tablas de multiplicar del 2 al 9

# for i in range(2, 10):
#     print(f"Tabla del {i}: ")
#     for j in range(1, 11):
#         m= i * j
#         print(f"{i} x {j} = {m}")
#     print("-"*30)

## Ejemplo 4 - Uso de break y continue

# for i in range (1, 21):
#     if i >= 10 and i <= 15:
#         continue
#     if i == 18:
#         break
#     print(i)
# print("Finalizado con éxito!!")

## Ejemplo 5 - Uso de exit()

# for i in range (1, 21):
#     if i >= 10 and i <= 15:
#         continue
#     if i == 18:
#         exit()
#     print(i)
# print("Finalizado con éxito!!")

## Ejemplo 6

# texto = "root:x:0:0:root:/root:/bin/bash"
# listatexto = texto.split(":")

# for i in texto.split(":"):
#     print(i)
    

# print(f"El usuario {listatexto[0]} tiene el ID {listatexto[2]}")