import os

from sedan import Sedan
from camioneta import Camioneta
from pickup import Pickup

def ingresar_sedan():
    marca = input('Ingrese la marca: ')
    linea = input('Ingrese la línea: ')
    modelo = int(input('Ingrese el modelo: '))
    propietario = input('Ingrese el propietario: ')
    carro = Sedan(marca, linea, modelo, propietario)
    return carro

def ingresar_camioneta():
    marca = input('Ingrese la marca: ')
    linea = input('Ingrese la línea: ')
    modelo = int(input('Ingrese el modelo: '))
    es_chocado = input('Indique si está "Chocado" o "No chocado": ')
    carro = Camioneta(marca, linea, modelo, es_chocado) 
    return carro

def ingresar_pickup():
    marca = input('Ingrese la marca: ')
    linea = input('Ingrese la línea: ')
    modelo = int(input('Ingrese el modelo: '))
    kilometraje = input('Ingrese el kilómetraje: ')
    carro = Pickup(marca, linea, modelo, kilometraje) 
    return carro

def mostrar_sedanes(sedanes):
    for sedan in sedanes:
        sedan.imprimir()
    input('Pulse una tecla para continuar...')

def mostrar_camionetas(camionetas):
    for camione in camionetas:
        camione.imprimir()
    input('Pulse una tecla para continuar...')

def mostrar_pickup(pickups):
    for pic in pickups:
        pic.imprimir()
    input('Pulse una tecla para continuar...')

sedanes = []
camionetas = []
pickups = []

while True:
    os.system('cls')
    print('--- Menú Principal ---\n')
    print('1. Igresar autos')
    print('2. Ver autos')
    print('3. Salir')
    opcion = int(input('Ingrese una opción: '))
    if opcion == 1:
        os.system('cls')
        print('¿Qué tipo de auto va ingresar?: ')
        print('1. Sedan')
        print('2. Camioneta')
        print('3. Pickup')
        print('4. Salir')
        opcion = int(input('Ingrese una opción: '))
        if opcion == 1:
            sedan = ingresar_sedan()
            sedanes.append(sedan) 
        elif opcion == 2:
            camionetass = ingresar_camioneta()
            camionetas.append(camionetass)
        elif opcion == 3:
            pickupss = ingresar_pickup()
            pickups.append(pickupss)
        elif opcion == 4:
            break
        else:
            continue
    elif opcion == 2:
        os.system('cls')
        print('¿Qué autos desea ver?: ')
        print('1. Sedan')
        print('2. Camioneta')
        print('3. Pickup')
        print('4. Salir')
        opcion = int(input('Ingrese una opción: '))
        if opcion == 1:
            mostrar_sedanes(sedanes)
        elif opcion == 2:
            mostrar_camionetas(camionetas)
        elif opcion == 3:
            mostrar_pickup(pickups)
        elif opcion == 4:
            break
        else:
            continue 
    elif opcion == 3:
        break
    else:
        continue