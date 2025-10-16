#!/home/jefe/scripts/miEnv/bin/python3

# 16.- Realizar un programa al que se le pasen tres números como parámetros y, con ellos, dibuje un triángulo. 
# Si los parámetros no van ordenados, el programa los tiene que ordenar.

from sys import argv
from colorama import Fore, Back, Style, init

init(autoreset=True) # Al terminar el print, vuelve al color por defecto


max = int(argv[1])
med = int(argv[2])
min = int(argv[3])

for i in range(1,max+1):
    s = ''
    for j in range(1,i+1):
        if j < 10:
            s += f" 0{j}"
        else:
            s += f" {j}"
    if i>=min and i<=med:
        print(Back.YELLOW + Fore.BLACK + Style.BRIGHT + s)
    else:
        print (s)

print (argv)