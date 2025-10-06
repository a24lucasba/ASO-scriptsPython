#!usr/bin/python3

from math import pi, pow

def perimetro(radio=''):
    calc = 2 * pi * radio
    salida = (f'El perímetro es de {calc} cm')
    return salida
def area(radio=''):
    calc = pi * pow(radio,2)
    salida = (f'El área es de {calc} cm²')
    return salida
def volumen(radio=''):
    calc = (4/3) * pi * pow(radio,3)
    salida = (f'El volumen es de {calc} cm³')
    return salida

##Elimina tildes ######################
import unicodedata
def eliminaTildes(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
########################################