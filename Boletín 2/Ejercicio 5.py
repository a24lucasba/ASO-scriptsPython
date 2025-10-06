#!/usr/bin/python3

from subprocess import run
run ('clear', shell=True)
from pathlib import Path
from datetime import datetime

# 5.- Escribir un programa que vaya solicitando al usuario que ingrese nombres.
#     a) Si el nombre se encuentra en la agenda (implementada con un diccionario), 
#       debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto y eliminar el contacto.
       
#     b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. 
#       El usuario puede utilizar la cadena "*", para salir del programa.
       
#     c) Guardar la agenda en un archivo de texto : miAgenda.txt

# 		pepe:685909090
# 		maria:123123123
# 		juan:987123456

#Deinimos un diccionario vacío donde guardamos nuestros contactos
dAgenda = {}
adAgenda = '/home/sanclemente.local/a24lucasba/ASO/agenda'
aAgenda = Path(adAgenda)


########################################### LEE EL ARCHIVO ###################################
#Si el archivo existe , rellenamos el diccionario con su contenido
if aAgenda.exists():
    with open (adAgenda) as fr: #Paso el archivo a una lista de líneas
        lA = fr.readlines()
        for l in lA: #Recorro la lista de líneas
            ll = l.split(':')
            k = ll[0].strip()
            v = ll[1].strip()
            dAgenda.setdefault(k,v) #Cada línea es un elemento de la agenda

######################################### EDITA EL ARCHIVO ######################################################

print ("Mi agenda de contactos")
while True:

    #Pedimos un nombre de contacto, * se termina de editar la agenda
    c = input("Introduce nombre ('*' para salir):")
    if c.strip() != '*':
        if c not in dAgenda:
            t = input(f"Teléfono de {c}: ")
            dAgenda.setdefault(c,t)
        else:
            print(f"{c} ya está en la Agenda con tlf {dAgenda[c]}")
            print("""¿Qué te interesa hacer?
                  1. Modificar el teléfono
                  2. Eliminar el contacto
                  Otra. No hacer nada
                  """)
            o = input("Opción: ")
            if o == '1':
                t = input(f"Nuevo teléfono de {c}: ")
                dAgenda[c]= t
            elif o == "2":
                print(f"Que se joda {c} ")
                dAgenda.pop(c)
            else:
                pass
    else:
        break


    #Estado de la agenda

    print('-'*30)
    for k,v in dAgenda.items():
        print(f"{k} : {v}")
    print('-'*30)

######################################### ACTUALIZA LOS DATOS EN EL ARCHIVO ######################################################

#Terminamos de rabajar con la Agenda y queremos guardar copia en archivo
#Si el diccionario está vacío que no haga nada
if dAgenda != {}:

#Antes pasamos el diccionario a string
    sAgenda = ''
    for k,v in dAgenda.items():
        sAgenda += f"{k}:{v}\n"
    # print (sAgenda)
    #Si existe el archivo lo borramos
    if aAgenda.exists():
        fecha = datetime.now()
        aAgenda.rename(f'/home/sanclemente.local/a24lucasba/ASO/{fecha.day}-{fecha.month}-{fecha.year}_{fecha.hour}:{fecha.minute}:{fecha.second}_agenda')
    #Añadimos el contenido del diccionario al archivo
    with open (adAgenda, 'w') as fw:
        fw.write(sAgenda)
else:
    pass
