from comprador import Comprador
from os import system

print('-----  CINE  -----')
nom = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
memb = input('Escriba "Si" o "No" dependiendo si posee una membresía: ')
persona = Comprador(nom, edad, memb)

while True:
    print('MENÚ')
    print('1. Visualizar al comprador')
    print('2. Verificar si puede ver una pelicula de miedo')
    print('3. Verificar el precio de la entrada')
    print('4. Verificar si la persona tiene poporopos gratis')
    print('5. Salir')
    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        system('cls')
        print(persona)
        input('Presione cualquier tecla para continuar...')
    elif opcion == 2:
        system('cls')
        es_mayor = persona.verificar_acceso()
        if es_mayor:
            print('Puede ver una pelicula de miedo. :O')
        else:
            print('No cumple con la edad o le falta una membresia.')
        input('Presione cualquier tecla para continuar...')
    elif opcion == 3:
        system('cls')
        precio = persona.verificar_precio()
        print(f"El precio de su entrada es: Q. {precio}")
        input('Presione cualquier tecla para continuar...')
    elif opcion == 4:
        system('cls')
        pop = persona.dar_poporopos()
        if pop:
            print('Tienes derecho poporopos gratis :)')
        else:
            print('Si quieres poporopos gratis adquiere tu membresia primero.')
        input('Presione cualquier tecla para continuar...')
    elif opcion == 5:
        break
    else:
        continue

