#!/home/jefe/scripts/miEnv/bin/python3

from subprocess import run

cpasswd = '/etc/passwd'
dInfoUsuarios = []

def infoUser(nombre):

    with open (cpasswd,'r') as fr:
        for l in fr:
            ll = l.split(':')

            user = ll[0]
            uid = ll[2]
            home = ll[5]

            cgroups = (f'groups {user}')
            scgroups = run(cgroups,shell=True, capture_output=True, text=True, check=True).stdout.split()

            gPrincipal = scgroups[2]
            gSecundarios = scgroups[3:]

            directorio = ll[6]
            cTamHome = f'du -sh {directorio}'
            scTamHome = run(cTamHome,shell=True, capture_output=True, text=True, check=True).stdout

            tamHome = scTamHome.split()[0]

            dInfoUsers = {
                'nombre':user,
                'uid':uid,
                'grupoPrin':gPrincipal,
                'grupoSec':gSecundarios,
                'home':home,
                'tamHome':tamHome
            }
            dInfoUsuarios.append(dInfoUsers)

    for usuario in dInfoUsuarios:
        if usuario['nombre'] == nombre:
            for k, v in usuario.items():
                print (f"{k}: {v}")
            break