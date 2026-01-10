from lista import Lista
import os
# Mario Daniel Sajvin Gómez
# Diana Melissa Morales Ruano 
# Keneth kanek López Pérez

print('---   Lista Ordenada   ---\n')
numeros = Lista()

while True:
    os.system('cls')
    print('1. Ingresar números')
    print('2. Salir')
    opcion = int(input('Ingrese una opción: '))
    if opcion == 1:
        os.system('cls')
        num = int(input('Ingrese un número: '))
        numeros.nuevo_insertar(num)
        print(numeros.recorrer())
        os.system('pause')
    elif opcion == 2:
        break
    else:
        continue