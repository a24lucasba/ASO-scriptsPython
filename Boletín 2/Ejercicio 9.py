#!/usr/bin/python3

from subprocess import run

run ("clear", shell=True)

# 9.- Crear una función para validación de contraseñas. Dicho módulo, deberá cumplir con los siguientes criterios de aceptación:
#     • La contraseña debe contener un mínimo de 8 caracteres .
#     • Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico 
#       (de estas cuatro condiciones debe cumplir tres) .
#     • La contraseña no puede contener espacios en blanco .
#     • Contraseña válida, retorna True .
#     • Contraseña no válida, retorna False .

password = input("Introduce una contraseña: ")

def validacion(p):
    conteo=0
    if len(p) >= 8:
        if (p.islower()):
            conteo+=1
        if (p.isupper()):
            conteo+=1
        if (any(char.isdigit() for char in p)):
            conteo+=1
        if (any(not char.isalnum() for char in p)):
            conteo+=1
        if conteo >= 3:
            if " " not in p:
                print ("Contraseña válida")
                return True
            else:
                print ("La contraseña no puede contener espacios en blanco")
                return False
        else:
            print ("La contraseña debe contener al menos 3 de las siguientes condiciones: letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")
            return False
    else:
        print ("La contraseña debe tener al menos 8 caracteres")
        return False

print (validacion(password))

