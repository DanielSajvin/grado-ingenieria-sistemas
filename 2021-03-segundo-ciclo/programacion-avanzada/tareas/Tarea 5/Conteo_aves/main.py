from observador import Observador
import os

clear = lambda: os.system('cls')

# Se le pide datos al usuario
for i in range(0, 7):
    num = Observador(int(input('Ingrese las aves vistas en la semana: ')))
    Observador.agregar(num)

while True:
    print('\nMenú')
    print('1. Contar las aves de la última semana')
    print('2. Contar las aves vistas hace 7 días')
    print('3. Calcular el total de aves vistas')
    print('4. Calcular el número de días ocupado')
    print('5. Salir')
    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        clear()
        print(Observador.contar_aves())
        input('Presione cualquier tecla para continuar...')
    elif opcion == 2:
        clear()
        print(Observador.dia())
        input('Presione cualquier tecla para continuar...')

    elif opcion == 3:
        clear()
        print(Observador.ultima_semana())
        input('Presione cualquier tecla para continuar...')
    elif opcion == 4:
        clear()
        Observador.dia_ocupado()
        input('Presione cualquier tecla para continuar...')  
    elif opcion == 5:
        break
    else:
        continue
