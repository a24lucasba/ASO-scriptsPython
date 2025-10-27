#!/home/jefe/scripts/miEnv/bin/python3

from re import findall
import ipaddress
from subprocess import run

run ('clear',shell=True)

dInfoAuthLog = {}
a = 'Tarea 4v2/auth.log'

ppl = r'for\s+.*(?:[0-9]{1,3}\.){3}[0-9]{1,3}'

with open(a,'r') as fr:
    for l in fr:
        if ': Failed password' in l:
            uEntro = False
        elif ': Accepted password' in l:
            uEntro = True
        else:
            continue

        lpl = findall(ppl,l)[0].split()
        ip = lpl[-1]

        if ' '.join(lpl[1:3]) == 'invalid user':
            usuario = lpl[3]
            if usuario == 'from':
                usuario = 'Blank'
        else:
            usuario = lpl[1]

        if ip not in dInfoAuthLog:
            dInfoIP =  {}
            uNo = []
            uSi = []

            dInfoIP.setdefault('privada',ipaddress.IPv4Address(ip).is_private)
            dInfoIP.setdefault('uNo',uNo)
            dInfoIP.setdefault('uSi',uSi)
            dInfoAuthLog.setdefault(ip,dInfoIP)
        else:
            pass
        
        if uEntro:
            if usuario not in dInfoAuthLog[ip]['uSi']:
                dInfoAuthLog[ip]['uSi'].append(usuario)
        else:
            if usuario not in dInfoAuthLog[ip]['uNo']:
                dInfoAuthLog[ip]['uNo'].append(usuario)

for k,v in dInfoAuthLog.items():
    print (f'{k}: {v}')