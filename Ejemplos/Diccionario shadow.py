#!/usr/bin/python3

aShadow = '/etc/shadow'
#Diccionrio shadow
##Clave : cuenta de usuario
##Valor : Si tiene o no password
dShadow = {}

with open(aShadow,'r') as fr:
    for l in fr:
        ll=l.split(":")
        dShadow.setdefault(ll[0], len(ll[1]) > 1) 

print (dShadow)