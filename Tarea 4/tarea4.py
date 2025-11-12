#!/home/jefe/scripts/miEnv/bin/python3

from subprocess import run
from re import findall
import ipinfo
import requests
from time import sleep

run ('clear',shell=True)

handler = ipinfo.getHandler('81a72251e9592e')

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
                    usuario = 'None'
            
            datos = handler.getDetails(ip)
            
            if hasattr(datos, 'loc') and datos.loc:
                lat = datos.loc.split(',')[0]
                lon = datos.loc.split(',')[1]
            else:
                lat = 'Desconocido'
                lon = 'Desconocido'
            
            ciudad = getattr(datos, 'city', 'Desconocido'),
            region = getattr(datos, 'region', 'Desconocido'),
            pais = getattr(datos, 'country_name', 'Desconocido'),
            latitud = lat.strip() if lat != 'Desconocido' else 'Desconocido',
            longitud = lon.strip() if lon != 'Desconocido' else 'Desconocido'

            if ip not in dInfoAuthLog:
                dInfoAuthLog[ip] = {'ciudad' : ciudad,'region':region,'pais':pais,'latitud':latitud,'longitud':longitud,'usuarios': [usuario]}
            else:
                if usuario not in dInfoAuthLog[ip]['usuarios']:
                    dInfoAuthLog[ip]['usuarios'].append(usuario)
                else :
                    pass

for k,v in dInfoAuthLog.items():
    print (f'{k}:{v}')