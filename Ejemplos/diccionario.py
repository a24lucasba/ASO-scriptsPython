#!usr/bin/python3

dPC = {
    "micro":"Intel Core i7",
    "ram":"DDR4",
    "disco":"M.2",
    "ramDisco":"1TB",
    "fuente":"aerocool"
}

for k in dPC:
    print(f"El valor de {k} es {dPC[k]}")


listaClaves = dPC.keys()
print(listaClaves)
listaValores = dPC.values()
print(listaValores)

for k,v in dPC.items():
    print(f"El valor de {k} es {v}")



dPC.setdefault("gpu","Nvidia")
dPC.pop("ramDisco") 

if "micro" in dPC:
    print (f'El nombre del microprocesador es {dPC['micro']}')
else:
    print ("Esa clave o existe en el diccionario")