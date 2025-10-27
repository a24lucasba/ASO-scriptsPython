#!/home/jefe/scripts/miEnv/bin/python3

from subprocess import run
from re import findall

run ('clear',shell=True)

a = 'Tarea 4v3/auth.log'

patip = r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}'

dInfoAuthLog = {}
exito = 1
fallo = 1

with open (a,'r') as fr:
    for l in fr:
        if ': Failed password' in l:
            uEntro = False
        elif ': Accepted password' in l:
            uEntro = True
        else:
            continue

        ip = findall(patip,l)[0]

        if ip not in dInfoAuthLog:
            dInfoIp = {}
            dInfoAuthLog.setdefault(ip,dInfoIp)
        else:
            if uEntro:
                exito = +1
            else:
                fallo =+1

        

        dInfoIp.setdefault('intentosTotales',exito + fallo)
        dInfoIp.setdefault('loginsExitosos',exito)
        dInfoIp.setdefault('loginsFallidos',fallo)
        



for k,v in dInfoAuthLog.items():
    print (f'{k}:{v}')