#!/home/jefe/scripts/miEnv/bin/python3

from subprocess import run
import unicodedata
from crypt import crypt, mksalt

run ('clear', shell=True)

def eliminar_tildes(texto):
    # Normaliza el texto y elimina los acentos
    texto_sin_tildes = unicodedata.normalize('NFD', texto)
    texto_sin_tildes = ''.join(c for c in texto_sin_tildes if unicodedata.category(c) != 'Mn')
    return texto_sin_tildes

a = 'Simulacro/usuarios.csv'

c = 'groups jefe'
sc = run(c,shell=True, capture_output=True, text=True, check=True).stdout.split(':')[1].split()
gruposSec = ','.join(sc)

with open(a,'r') as fr:
    next(fr)  # Saltar la primera línea (cabecera)
    for l in fr:
        ll = l.split(',')
        nome = eliminar_tildes(ll[2].lower().replace(' ',''))
        ape1 = list(ll[0])[0].lower()
        ape2 = list(ll[1])[0].lower()
        año1 = list(ll[6])[-2]
        año2 = list(ll[6])[-1]

        user = f'a24{nome}{ape1}{ape2}{año1}{año2}'
        password = ll[5]
        passCifrada = crypt(password,mksalt())

        if ll[7].strip() != '':
            grupoPrin = ll[7].lower().strip()
            cmd = ['useradd', user, '-g', grupoPrin, '-G', f'alumnos,{gruposSec}', '-s', '/bin/bash', '-m', '-d', f'/home/{user}', '-p', passCifrada]
            run(cmd)
        else:
            grupoPrin = 'alumnos'
            cmd = ['useradd', user, '-g', grupoPrin, '-G', gruposSec, '-s', '/bin/bash', '-m', '-d', f'/home/{user}', '-p', passCifrada]
            run(cmd)            


        