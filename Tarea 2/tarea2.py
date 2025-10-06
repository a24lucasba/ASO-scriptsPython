#!/usr/bin/python3

# ASO – Primera Evaluación – Tarea 2 - Python

from subprocess import run
run ('clear', shell=True)
from pathlib import Path
from datetime import datetime
	
# Programa un script que ejecute el comando:
# 	$ top -bn1 -o %MEM


# Debes guardar en un archivo csv con nombre: top_aaaa_mm_dd_hh_mm.csv 
# 		→ Módulo 'datetime' para fechas

dCSV = {}
adCSV = f'Tarea 2/top_{datetime.year()}_{datetime.month}_{datetime.day}_{datetime.hour}_{datetime.minute}.csv)'
aCSV = Path(adCSV)

# En ese archivo csv debes guardar los campos:
# USER;COMMAND;%CPU;%MEM;PID;PPID


# Pero solamente de los comandos que consuman más de 0% de memoria


# Para el cálculo del PPID utilizar el comando:
# 	$ ps -f PID

# Si este comando no da salida para algún PID poner PPID = “null”


# Ejemplo de salida:
# Generado archivo:top_24_11_2021_07_54.csv

# USER;COMMAND;%CPU;%MEM;PID;PPID
# root;systemd-journal;0,0;1,5;181;1
# root;systemd;0,0;1,0;1;0
# ladmin;python3;0,0;1,0;1991;574
# root;sshd;0,0;0,9;567;422
# root;sshd;0,0;0,9;1276;422
# root;wpa_supplicant;0,0;0,5;282;1
# ladmin;bash;0,0;0,5;563;421
# root;login;0,0;0,4;421;1
# ladmin;sftp-server;0,0;0,4;1049;1048
# ladmin;sftp-server;0,0;0,4;878;877
# root;rsyslogd;0,0;0,4;273;1
# ladmin;top;0,0;0,4;1993;null
# root;VBoxService;0,0;0,3;508;1
# root;cron;0,0;0,3;258;1
# ladmin;(sd-pam);0,0;0,3;545;544
# ladmin;sh;0,0;0,1;1992;1991


# Nota : Preparación:1, Datos top:4, Nombre archivo:1, Datos ps:2, CSV:2


# Ayudas: 
# → Para substituir uno o múltiples espacios por un ‘;’ utilizar : 
# 	textoSalida = re.sub(‘\s+’, ‘;’, texto)


########################### Creamos / actualizamos los datos del archivo ##########################
if dCSV != {}:

#Antes pasamos el diccionario a string
    sCSV = ''
    for k,v in dCSV.items():
        sCSV += f"{k}:{v}\n"
    # print (sCSV)
    #Si existe el archivo lo borramos
    if aCSV.exists():
        aCSV.rename(f'top_{datetime.year()}_{datetime.month}_{datetime.day}_{datetime.hour}_{datetime.minute}.csv')
    #Añadimos el contenido del diccionario al archivo
    with open (adCSV, 'w') as fw:
        fw.write(sCSV)
else:
    pass
