#!/usr/bin/python3

from subprocess import run
from requests import get
from time import sleep

run('clear',shell=True)

# subred = input("Introduce la ip a estudiar: ")

cping = f"fping -g 192.168.0.0/24 -a -q -e"

scping = run(cping,shell=True, capture_output=True, text=True).stdout.strip().split('\n')

for l in scping:
    ip = l.split()[0]
    latencia = l.split()[1]

    cneigh = f"ip neigh show {ip}"
    scneigh = run(cneigh,shell=True,text=True,capture_output=True).stdout.split(' ')

    try:
        mac = scneigh[4]
    except:
        mac = "08:00:27:10:0e:1c"

    sleep(1.5)
    resp = get(f'https://api.macvendors.com/{mac}')
    fabricante = resp.text
    print (fabricante)