#!//usr/bin/python3

pathArchivo = '/proc/meminfo'
dMemInfo = {}

with open(pathArchivo, 'r') as fr:
    for l in fr:
        ll = l.split(':') #Divido la línea en una lista de dos campos
        k = ll[0].strip() #Clave = Elemento 0 de la lista y limpio
        if len(ll) == 2:
            v = ll[1].strip() #Valor = Elemento 1 de la lista y limpio
        else:
            v = '' #Si no hay valor, lo popnemos con un string vacío
        dMemInfo.setdefault(k,v)
#Vemos el contenido del diccionario MemInfo

print(dMemInfo)