from cuenta import Cuenta

print(' \n----- BIENVENIDO AL BANCO SJNV ----- \n')
print('Ingrese sus datos para crear una cuenta')
titular = input("Titular de la cuenta: ")
numero = input('Número de cuenta: ')
saldo = float(input('Ingrese el saldo:  '))

cuenta = Cuenta(titular, numero, saldo)

while True: 
    print('\nAcciones: ')
    print('1- Mostrar saldo.')
    print('2- Depositar.')
    print('3- Retirar.')
    print('4- Historial de movimientos.')
    print('5- Salir.')
    opcion = int(input('Seleccione una opcion: \n'))

    if opcion == 1:
        print(cuenta)

    elif opcion == 2:
        cantidad = float(input('¿Cuántos desea depositar?: \n'))
        cuenta.depositar(cantidad)
    
    elif opcion == 3:
        cantidad = float(input('¿Cuánto desea retirar?: \n'))
        if cantidad <= saldo:
          cuenta.retirar(cantidad)
        else:
            print('NO TIENE FONDOS NECESARIOS PARA RETIRAR.')
            
    elif opcion == 4:
        cuenta.mostrar_movimientos()

    elif opcion == 5:
        break
    else:
        continue