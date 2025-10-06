#!/usr/bin/python3


# 8.- Crear una función para validación de nombres de usuarios. Dicha función, deberá cumplir con los siguientes criterios de aceptación:
#     • El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12 .
#     • El nombre de usuario debe ser alfanumérico .
#     • Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El nombre de usuario debe contener al menos 6 caracteres" .
#     • Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre de usuario no puede contener más de 12 caracteres" .
#     • Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El nombre de usuario puede contener solo letras y números" .
#     • Nombre de usuario válido, retorna True .

#Función validación nombres de usuario######################################################################################################
def nombreValido(nombre):
    #La salida es un diccionario con dos claves:
    ## valido = True/False
    ## mensaje = ""
    valido = False
    if not nombre.isalnum():
        mensaje = "El nombre de usuario puede contener solo letras y números"
    elif len(nombre) < 6:
        mensaje = "El nombre de usuario debe contener al menos 6 caracteres"
    elif len(nombre) > 12:
        mensaje = "El nombre de usuario no puede contener más de 12 caracteres"
    else:
        valido = True
        mensaje = "Nombre de usuario correcto"
    
    #Creamos el diccionario de salida
    salida = {}
    salida.setdefault("valido", valido)
    salida.setdefault("mensaje", mensaje)
    return salida
###########################################################################################################################################

n = input("Dame un nombre de usuario: ")
print (nombreValido(n)["valido"])
if nombreValido(n)["valido"]:
    print("Nombre válido")
else:
    print ("No válido")
    print (nombreValido(n)["mensaje"])