#!/usr/bin/python3

from subprocess import run

# 3.- Crear una lista de diccionarios con la información de los usuarios que tienen 
# UID >= 1000 <= 60000 y UID == 0 … 
# Los datos a guardar son: cuenta, uid, grupoPrincipal, gruposSecundarios, pathHome,
#  tamHome, shell, password (True o False).

infoUsuarios = []
aPasswd = open("/etc/passwd", "r")

aShadow = '/etc/shadow'
dShadow = {}
with open(aShadow,'r') as fr:
    for l in fr:
        ll=l.split(":")
        dShadow.setdefault(ll[0], len(ll[1]) > 1) 

for l in aPasswd:

    datos = l.split(":")

    uid = int(datos[2].strip())

    if uid==0 or (uid >= 1000 and uid <= 60000):

        cuenta = datos[0].strip()

        home = datos[5].strip()

        shell = datos[6].strip()

        gCuenta = run (f"groups {cuenta}", shell=True, capture_output=True, text=True, check=True).stdout
        gCuenta = gCuenta.split()
        gPrincipal = gCuenta[2].strip()
        gSecundario = gCuenta[3:]

        tamHome = run (f'du -hs {home}', shell=True, capture_output=True, text=True, check=True).stdout.split()
        tamHome = tamHome[0]


        infoUsuarios.append({"cuenta": cuenta, "uid": uid, "Grupo Principal": gPrincipal, "Grupo Secundario": gSecundario, "pathhome": home, "tamHome":tamHome, "shell": shell, "password": dShadow[cuenta]})
    else:
        pass

print (infoUsuarios)
