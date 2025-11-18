#!/usr/bin/python3

from subprocess import run
from requests import get
from time import sleep
from datetime import datetime
from os import path,makedirs

run('clear',shell=True)

subred = input("Introduce la ip a estudiar: ")

lInfoIps = []

cping = f"fping -g {subred} -a -q -e"

scping = run(cping,shell=True, capture_output=True, text=True).stdout.strip().split('\n')

for l in scping:
    ip = l.split()[0]
    latencia = l.split()[1]

    cneigh = f"ip neigh show {ip}"
    scneigh = run(cneigh,shell=True,text=True,capture_output=True).stdout.split(' ')

    try:
        mac = scneigh[4]
    except:
        mac = "f0:b6:1e:05:dc:c3" # Aquí iría la mac del equipo

    sleep(1.5)
    resp = get(f'https://api.macvendors.com/{mac}')
    fabricante = resp.text

    dInfoIps = {"ip":ip,"mac":mac,"fabricante":fabricante,"latencia":latencia}
    lInfoIps.append(dInfoIps)

fecha = datetime.now()
subredCortada = list(subred)[:-3]
a = f'hostsRed_{subredCortada}_{fecha.year}_{fecha.month}_{fecha.day}_{fecha.hour}_{fecha.minute}'

with open(f'Tarea 3/{a}','w') as fr:
        fr.write(f'ip;mac;fabricante;latencia\n')
        for l in lInfoIps:
            fr.write(f"{dInfoIps['ip']};{dInfoIps['mac']};{dInfoIps['fabricante']};{dInfoIps['latencia']}")
    