#!/usr/bin/python3

# ASO – Primera Evaluación – Tarea 2 - Python

from subprocess import run
from pathlib import Path
from datetime import datetime
from re import sub
	
run ('clear', shell=True)
# Programa un script que ejecute el comando:
# 	$ top -bn1 -o %MEM

sSalida = "USER;COMMAND;%CPU;%MEM;PID;PPID\n"

c = "top -bn1 -o %MEM"
sc = run (c, shell=True, capture_output=True, text=True).stdout

lsc = sc.split('\n') # Convierto la salida en una lista de lineas

# Debes guardar en un archivo csv con nombre: top_aaaa_mm_dd_hh_mm.csv
    #   → Módulo 'datetime' para fechas

fecha = datetime.now()
fileCSV = f'top_{fecha.year}_{fecha.month}_{fecha.day}_{fecha.hour}_{fecha.minute}_{fecha.second}.csv'

# En ese archivo csv debes guardar los campos:
# USER;COMMAND;%CPU;%MEM;PID;PPID
# Pero solamente de los comandos que consuman más de 0% de memoria
# Para el cálculo del PPID utilizar el comando:
# 	$ ps -f PID
# Si este comando no da salida para algún PID poner PPID = “None”
# Ayudas: 
# → Para substituir uno o múltiples espacios por un ‘;’ utilizar : 
# 	textoSalida = re.sub(‘\s+’, ‘;’, texto)

for l in lsc[7:]: # A partir de la linea 7 están los procesos
    # Cada linea tiene estos campos:
    # PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    ll = sub(r'\s+',';',l.strip()).split(';')
    if len(ll) == 12: # Solo me interesan las lineas con 12 campos
        mem = ll[9]
        if mem == '0,0': # Si la memoria es 0,0 salimos del bucle
            break
        else:
            user = ll[1].strip()
            command = ll[11].strip()
            cpu = ll[8].strip()
            pid = ll[0].strip()

            # Calculamos el PPID
            try:
                cPPID = f'ps -f {pid}'
                scPPID = run (cPPID, shell=True, capture_output=True, text=True).stdout
                ppid = sub(r'\s+',';',scPPID.split('\n')[1]).split(';')[2]
            except:
                ppid = 'None'



            # Vamos creando la nueva linea del string salida
            sls = f'{user};{command};{cpu};{mem};{pid};{ppid};\n'
            sSalida += sls

############################# Creamos el archivo ###################################

with open(f"./Tarea 2/{fileCSV}","w") as fileCSVw:
    fileCSVw.write(sSalida)
