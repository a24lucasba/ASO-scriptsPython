#!/usr/bin/python3

# 7.- Programa que lee lineas de varios archivos con extensión .data existentes en el directorio de trabajo. 
# Les calcula, por línea, el máximo, el mínimo y la media. 
# Esos cálculos los guarda en un archivo que se llama igual que el de lectura, pero que le añade al final,'out'. 
# Guarda los archivos de salida en un directorio que se pide como parámetro... si no existe el directorio se llama 'out'.

from glob import glob

archivos = glob("Boletín 2/Ejercicio 7/datos/*.data")
datos = {}
for file in archivos:
    with open(file) as contenido:
        contenido = contenido.read().split('\n')

