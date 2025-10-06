#!usr/bin/python3

# 3.- Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “abc123..” 
# se indica “Has entrado al sistema”, si no es así se da un error de usuario y/o contraseña no válidos.

from getpass import getpass
from subprocess import run
from hashlib import sha512

run("clear", shell=True)

usuario= "pepe"
#El password vamos a guardarlo en un hash SHA512
##La contraseña la codificamos en UTF-8
##luego aplicamos la función sha512 para generar el hash
##ese hash son 512 bytes que necesitamos guardar de algún modo
##para ello los pasamos a hexadecimal con la función hexdigest()
passUsuario= sha512("abc123.." .encode("utf-8")).hexdigest()

#Comprobamos inicio de sesion
print("Inicio de sesión del sistema")
#Pedimos datos de conexión
u = input("Usuario: ")
p = sha512(getpass("Contraseña: ").encode("utf-8")).hexdigest()

if u == usuario and p == passUsuario:
    print("Has entrado al sistema")
else:
    print("Error: Usuario y/o contraseña no válidos")