#!/usr/bin/python3

# Importamos la función run para ejecutar comandos del sistema
from subprocess import run

# Limpiamos la pantalla para una mejor visualización
run('clear',shell=True)

# PASO 1: Obtener la lista de discos disponibles en el sistema
# Creamos una lista vacía para almacenar los nombres de los discos
ld = []

# Ejecutamos el comando 'fdisk -l' para obtener información de todos los discos
c = 'fdisk -l'
sc = run(c,shell=True,capture_output=True,text=True,check=True).stdout

# Procesamos la salida línea por línea para encontrar los discos
for l in sc.split('\n'):
    # Las líneas que empiezan con 'Disco' contienen información de discos
    # Ejemplo: "Disco /dev/sda: 20 GiB, 21474836480 bytes, 41943040 sectores"
    if l.startswith('Disco'):
        # Extraemos el nombre del disco (ej: /dev/sda) que está en la posición 1
        # strip(':') elimina los dos puntos del final
        ld.append(l.split()[1].strip(':'))

####################### Lista de discos hecha #################

# PASO 2: Obtener información detallada de cada disco
# Creamos una lista para almacenar la información completa de todos los discos
lInfoDiscos = []

# Iteramos sobre cada disco encontrado para obtener su información detallada
for disco in ld:
    # Creamos un diccionario para almacenar toda la información de este disco
    dInfoDisco = {}
    # Guardamos el nombre del disco como primer elemento
    dInfoDisco.setdefault('disco',disco)
    # PASO 3: Obtener información específica del disco actual
    # Ejecutamos fdisk con --bytes para obtener información detallada en bytes
    c = f'fdisk -l --bytes {disco}'
    sc = run(c,shell=True,capture_output=True,text=True,check=True).stdout
    
    # Inicializamos variables para almacenar la información del disco
    tipoDisco = None  # Los discos no siempre tienen tipo, así que por defecto es None
    particiones = []  # Lista para almacenar información de las particiones
    # PASO 4: Procesar cada línea de la salida de fdisk para extraer información
    for l in sc.split('\n'):
        # Líneas que empiezan con 'Disco' contienen el tamaño del disco
        # Ejemplo: "Disco /dev/sda: 20 GiB, 21474836480 bytes, 41943040 sectores"
        if l.startswith('Disco'):
            # Extraemos el tamaño en bytes que está después de la primera coma
            # split(',')[1] obtiene "21474836480 bytes", luego split()[0] obtiene "21474836480"
            dInfoDisco.setdefault('tamDisco',l.split(',')[1].strip().split()[0])

        # Líneas que empiezan con 'Tipo' contienen el tipo de tabla de particiones
        # Ejemplo: "Tipo de etiqueta de disco: dos"
        elif l.startswith('Tipo'):
            # Extraemos el tipo que está después de los dos puntos
            tipoDisco = (l.split(':')[1].strip())
            dInfoDisco.setdefault('tipoDisco',tipoDisco)

        # Líneas que empiezan con el nombre del disco contienen información de particiones
        # Ejemplo: "/dev/sda1  *     2048   1050623   524288  83 Linux"
        elif l.startswith(f'{disco}'):
            # Creamos un diccionario para almacenar información de esta partición
            dInfoParticion = {}
            activa = False  # Por defecto la partición no está activa (no es booteable)
            
            # Dividimos la línea en campos separados por espacios
            ll = l.split()
            # El primer campo es siempre el nombre de la partición
            dInfoParticion.setdefault('particion',ll[0].strip())
            
            # Defiinimos una variable con el nombre de la particion
            particion = ll[0].strip()

            # Si el segundo campo es '*', significa que la partición es activa/booteable
            if ll[1].strip() == '*':
                activa = True
                # Eliminamos el asterisco de la lista para que los índices sean correctos
                ll.pop(1)
            
            # Guardamos la información de la partición
            dInfoParticion.setdefault('activa',activa)
            # El tamaño de la partición está en el índice 4 (después de ajustar por el *)
            dInfoParticion.setdefault('tamParticion',ll[4])
            # El tipo de partición son todos los campos desde el índice 6 en adelante
            tipoParticion = (" ".join(ll[6:]))
            dInfoParticion.setdefault('tipoParticion',tipoParticion)

            fs = None
            porcenOcup = None
            puntoMontaje = None
            if tipoParticion == 'Extendida' or 'swap' in tipoParticion:
                pass
            else:
            # Más información de las particiones con el comando df -Th {particion}
                cdf = f"df -Th {particion}"
                scdf = run(cdf,shell=True,capture_output=True,text=True,check=True).stdout
                llscdf = (scdf.split('\n')[1].split())
                fs = llscdf[1]
                porcenOcup = llscdf[5]
                puntoMontaje = llscdf[6]

            dInfoParticion.setdefault('fs',fs)
            dInfoParticion.setdefault('porcenOcup',porcenOcup)
            dInfoParticion.setdefault('puntoMontaje',puntoMontaje)



            # Agregamos la información de esta partición a la lista de particiones
            particiones.append(dInfoParticion)
        else:
            # Líneas que no nos interesan (cabeceras, espacios en blanco, etc.)
            pass
    
    # PASO 5: Completar la información del disco actual
    # Agregamos la lista de particiones al diccionario del disco
    dInfoDisco.setdefault('particiones',particiones)
    # Agregamos toda la información de este disco a la lista principal
    lInfoDiscos.append(dInfoDisco)



for dd in lInfoDiscos:
    print(dd)