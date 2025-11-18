#!/usr/bin/python3

from subprocess import run

run ('clear',shell=True)
def funcionInfoDiscos():
    c1 = 'fdisk -l'
    sc1 = run(c1,shell=True,capture_output=True,text=True).stdout.strip().split('\n')
    dInfoDiscos = {}
    lDiscos = []

    equipo = run('hostname',shell=True,capture_output=True,text=True).stdout.strip()
    dInfoEquipos = {'equipo':equipo,'discos':lDiscos}

    for l in sc1:
        if 'Disco ' in l:
            disco = l.split(' ')[1].strip(':')
            tamDisco = int(l.split(' ')[4])
            lParticiones = []
        if "Modelo" in l:
            modelo = l.split(':')[1].strip()

            dInfoDiscos = {"disco": disco,"tamDisco":tamDisco,"modeloDisco":modelo,"particiones":lParticiones}
            lDiscos.append(dInfoDiscos)

            c2 = f"fdisk -l --bytes {disco}"
            sc2 = run(c2,shell=True,capture_output=True,text=True).stdout.strip().split('\n')

            for l in sc2[9:]:
                if "Extendida" not in l:
                    if "swap" not in l:
                        particion = l.split()[0]
                        tamParticion = l.split()[-3]

                        if l.split()[-1] == "Linux":
                            tipo = "ext4"
                        else:
                            tipo = l.split()[-1]
                    
                        c3 = f"df -Th {particion}"
                        sc3 = run(c3,shell=True,capture_output=True,text=True).stdout.strip().split('\n')[1]
                        pMontajeParti = sc3.split()[-1]

                        dInfoParticiones = {"particion":particion,"tamParticion":tamParticion,"fsParti":tipo,"pMontajeParti":pMontajeParti}
                        lParticiones.append(dInfoParticiones)

    return dInfoEquipos
    

print (str(funcionInfoDiscos()).replace("}]}, ","}]}, \n\n").replace("'discos': [","'discos': [\n\n"))