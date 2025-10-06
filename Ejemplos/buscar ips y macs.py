#!/usr/bin/python3


from subprocess import run
from re import compile,findall, IGNORECASE

c = "ip a show enp0s3"
sc = run(c, shell=True, capture_output=True, text=True).stdout
print (sc)

pIP = compile(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}")
lIP = pIP.findall(sc)
pMAC = compile(r"(?:[0-9A-F]{2}[:-]){5}[0-9A-F]{2}",IGNORECASE)
lMAC = pMAC.findall(sc)


print (lIP)
print (lMAC)