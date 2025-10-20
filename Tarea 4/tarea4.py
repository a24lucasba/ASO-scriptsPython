#!/home/jefe/scripts/miEnv/bin/python3

from subprocess import run
from re import findall

run ('clear',shell=True)

patronIP = r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
buscarUser = r'Failed password for (.*)'
rutaArchivo = 'Tarea 4/auth.log'
dInfoAuthLog = {}
dInfoIP = {}

with open(rutaArchivo, 'r') as fr:
    for l in fr:
        if "Failed password for" in l:
            l = l.strip()
            ip = findall(patronIP, l)[0]

            lUsu = findall(buscarUser,l)[0]
            

            if not lUsu.startswith('invalid user'):
                usuario = lUsu.split()[0]
            else:
                if not lUsu.split()[2]=='from':
                    usuario = lUsu.split()[2]
                else:
                    usuario = 'Blank'

            if ip not in dInfoAuthLog:
                dInfoAuthLog[ip] = {'usuarios': [usuario]}
            else:
                if usuario not in dInfoAuthLog[ip]['usuarios']:
                    dInfoAuthLog[ip]['usuarios'].append(usuario)
                else :
                    pass

for k,v in dInfoAuthLog.items():
    print (f'Clave: {k}, Valor: {v}')
