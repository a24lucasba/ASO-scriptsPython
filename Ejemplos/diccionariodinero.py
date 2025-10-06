# !/usr/bin/python

# Dada una cantidad de dinero introducida por el usuario, se devuelve un diccionario con la cantidad de billetes
#  y monedas de curso legal mínimos necesarios que suman ese valor (ya sin céntimos):
#   738€ = {500:1,  200:1, 100:1, 50:0, 20:1, 10:1, 5:1, 2:1, 1:1}

# dineros={}
# lBiMo={500,200,100,50,20,10,5,2,1}

# cantidad = 1238

#Si lo hacemos restando:
# Recorremos la lista de lBiMo empezando por el de mayor valor:

# 1238 -500 = 728 --- Es negativo este valor? NO --- La clave 500 esdtá en el diccionario? NO ---
# añadimos la clave 500 con valor 1 : dineros.setdefault[500,1]
# Seguimos:
# 738 -500 = 238 --- Es negativo este valor? NO --- La clave 500 está en el diccionariio? Sí ---
# al valor de la clave 500 le añadimos 1 y actalizamos la clave: dinero[500] = dinero[500] + 1
# Seguimos:
# 238 - 500 = -62 --- Es negativo este valor? SÍ  --- Pasamos a la siguiente clave ---
# 238 - 200 = 38 --- dinero = {500:2,200:1} ---
# Así hasta que el resto sea igual a 0

#Si lo hacemos dividiendo:
# Recorremos la lBiMo empezando por el de mayor 
# 1238/500 = 2,476 --- Seleccionamos el entero (truncamos) y ese será el valor de la clave 500
# dineros.setdefault(500,2)
#Actualizamos la cantidad de dinero que falta por asignar
# 1238 - (500*2) = 238
# Pasamos al siguiente elemento de la lBiMo
# 238 / 200 = 1,19 ... Seleccionamos el entero (truncamos) y ese será el valor de la clave 500
# dineros.setdefault(200,1)
# 238 - (200*1) = 38
# Pasamos al siguiente elemento de la lBiMo
# 38 / 100 = 0,38 Seleccionamos el entero (truncamos) y ese será el valor de la clave 500
# dineros.setdefault(100,0) o directamente no se añade
# Seguimos con 38 ... Hasta llegar a 0

dineros={}
lBiMo=[500, 200, 100, 50, 20, 10, 5, 2, 1]

cantidad = 1238


for i in lBiMo: # Recorremos la lista de billetes y monedas empezando por el de mayor valor
    num=cantidad//i # Dividimos la cantidad entre el valor del billete o moneda, al poner // nos quedamos con la parte entera
    dineros.setdefault(i,num) # Añadimos al diccionario la clave (valor del billete o moneda) y el valor (número de billetes o monedas)
    cantidad=cantidad-num*i # Actualizamos la cantidad de dinero que falta por asignar

print (dineros)