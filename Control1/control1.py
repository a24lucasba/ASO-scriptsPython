#!/usr/bin/python3

from subprocess import run

def getProcesos(): 
    ctop = 'top -bn1 -o %MEM' # Comando inicial para obtener los datos de procesos
    sctop = run(ctop,shell=True,capture_output=True,text=True).stdout 

    listaTop = sctop.split('\n')[7:]    # Meto la salida del comando en una lista y me quedo solo con los datos que quiero, a partir de la línea 8
    ldpid = {}

    for l in listaTop: # Recorro la lista por líneas
        ll = l.split()  # Convierto las líneas n una lista para poder acceder a cada elemento
        if ll != []:    # La última línea era una lista vacía, con esto la elimino
            mem = (ll[9])
            mem = float(mem.replace(',','.'))   # Convierto los valores en float
            if mem > 0.0:   # Cojo los procesos que consuman más de 0.0% de memoria
                comando = ll[11]
                usuario = ll[1]
                cpu = float(ll[8].replace(',','.')) # Convierto los valores en float, para ello necesito reemplazar las comas por puntos
                pid = ll[0]

                cps = f'ps -f {pid}'    # Comando para sacar el ppid
                scps = run(cps,shell=True,capture_output=True,text=True).stdout
                
                try: 
                    ppid = int((scps.split('\n')[1].split()[2]))    # Si existe el ppid actualizamos la variable
                except:
                    ppid = None     # Si no exite el ppid este es igual a None

                dpid ={                         # Defino el subdiccionario que va a estar dentro del diccionario principal
                    'comando' : comando,
                    'usuario' : usuario,
                    'cpu' : cpu,
                    'mem' :  mem,
                    'ppid' : ppid
                }
                ldpid.setdefault(pid,dpid)      # Diccionario principal clave(pid):valor(subdiccionario)

    lsalida = []                        # Todo esto es para que la salida de la funcion sea agradable a la vista
    for k,v in ldpid.items():
        lsalida.append(f'{k} : {v}\n') # En vez de que la salida sea el diccionario hago que sea un string y haga un salto de linea para cada clave:valor
                                       # y lo meto en una lista auxiliar
    
    salida = ''.join(lsalida) # Aquí hago lo mismo con la lista auxiliar del paso anterior

    return f'\n{salida}'
