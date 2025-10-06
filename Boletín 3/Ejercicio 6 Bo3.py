#!/usr/bin/python3


# 6.- Crear un script en python que nos permita dar de alta usuarios en un equipo linux desde un csv separado por comas (usuarios.csv) : 
#        - Crear un nombre de usuario único 'a23[PrimerNombre][PrimerasLetras]'.
#        -- Ver si existe ya en el /etc/passwd y… si es así… cambiarle de nombre…
#            'a23[PrimerNombre][PrimerasLetras][Numero]'
#        - Contraseña "abc123..".
#        - Que pertenezcan al grupo primario “alumnos” que tienes que crear antes.
# 	- Que pertenezca a los mismos secundarios que el usuario jefe.
#        - home único para cada usuario.
#        - /bin/bash como shell por defecto...
# Comando:
# $ useradd -d /home/cuenta -m -g alumnos -G [listaGruposSeparadosPorComas] -s /bin/bash -p [passwordCifrada] cuenta

from subprocess import run
from crypt import crypt, mksalt, METHOD_SHA512
from misFunciones import eliminaTildes


# Descubrimos los grupos secundarios del usuario jefe

c = "groups jefe"
sc = run(c, shell=True, capture_output=True, text=True, check=True).stdout
gSec = sc.split()[3:]
gSec = ','.join(gSec)


# Contraseña "abc123.."

password = "abc123.."


# Leemos el archivo usuarios.csv y lo ponemos a una lista de líneas

aU = 'usuarios.csv'
with open(aU, 'r') as fr:
    lAu = fr.readlines()

###################### Ya lo tenemos en una lista de líneas ####################

# Recorremos la lista saltándonos la primera línea

for l in lAu[1:]:
    print (l)
    ll = l.split(';')
    cuenta = eliminaTildes(f"a25{ll[2].split()[0]}{ll[0][0]}{ll[1][0]}{ll[7][-2:]}".lower())
    print (cuenta)

    # Genera un salt aleatorio y cifra la contraseña

    salt = mksalt(METHOD_SHA512)
    password_cifrada = crypt(password, salt)

    # Vamos creando el comando useradd:

    c = f'useradd -d /home/{cuenta} -m -g alumnos -G {gSec} -s /bin/bash -p \'{password_cifrada}\' {cuenta}'
    print (c)

    # Ejecutamos el comando
    run(c, shell=True, check=True)

    print ("-"*50)
