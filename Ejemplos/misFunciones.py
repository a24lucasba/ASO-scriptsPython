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
def dameDNI():
    from random import randint

    POSSIBLE_LETTERS = ("T","R","W","A","G","M","Y","F",
        "P","D","X","B","N","J","Z","S","Q","V","H",
        "L","C","K","E","T",)
    NUMBER_DNI = randint(10000000, 99999999)
    LETTER_DNI = POSSIBLE_LETTERS[NUMBER_DNI % 23]
    return f"{NUMBER_DNI}{LETTER_DNI}"
####################################################

#################################################################################################
def dameUsuarios(n):
    from faker import Faker
  
    fake = Faker('es_ES')
    lUsuarios = []

    for _ in range(n):
        dTemp = {}
        dTemp.setdefault('nombre', fake.name())
        dTemp.setdefault('cumple', fake.\
        date_of_birth(tzinfo=None, minimum_age=18, maximum_age=55).strftime("%d-%m-%Y"))
        dTemp.setdefault('direccion', fake.address().replace('\n',' '))
        dTemp.setdefault('telefono', fake.phone_number())
        dTemp.setdefault('trabajo', fake.job())
        dTemp.setdefault('dni', dameDNI())
        lUsuarios.append(dTemp)

    return lUsuarios
#################################################################################################