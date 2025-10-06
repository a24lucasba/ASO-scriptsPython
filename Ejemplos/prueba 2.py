#!/usr/bin/python3

from subprocess import run

usuario = "ladmin"
grupoPrincipal = ''
grupoSecundario = []
comando = f'groups {usuario}'

salida = run (comando, shell=True, capture_output=True, text=True, check=True).stdout

grupoPrincipal = salida.split(':')[1].strip().split(' ')[0]
grupoSecundario = salida.split(':')[1].strip().split(' ')[1:]

print (grupoPrincipal)
print (grupoSecundario)
