from visitante import Visitante
from os import system

print('-----  PARQUE DE DIVERSIONES  -----\n')
nom = input('Ingrese su nombre: ')
alt = int(input('Ingrese su altura en centímetros: '))
persona = Visitante(nom, alt)

while True:
    print('\nMENÚ')
    print('1. Visualizar al visitante')
    print('2. Comprar pase de atracciones')
    print('3. Revocar el pase de atracciones')
    print('4. Verificar si el visitante puede subir a una rueda')
    print('5. Salir')
    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        system('cls')
        print(persona)
        input('Presione cualquier tecla para continuar...')
    elif opcion == 2:
        system('cls')
        print(persona.comprar())
        input('Presione cualquier tecla para continuar...')
    elif opcion == 3:
        system('cls')
        print(persona.revocar())
        input('Presione cualquier tecla para continuar...')
    elif opcion == 4:
        system('cls')
        altura_permitida = int(input('Ingrese la altura mininima en cm: '))
        persona.verificar(altura_permitida)
        print(persona.verificar(altura_permitida))
        input('Presione cualquier tecla para continuar...')
    elif opcion == 5:
        break
    else: 
        continue