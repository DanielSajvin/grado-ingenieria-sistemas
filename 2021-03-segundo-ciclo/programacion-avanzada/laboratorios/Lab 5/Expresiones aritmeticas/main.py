from pila import Pila
from operador import Operador
import os

print('-----   EXPRESIONES ARITMETICAS   -----\n')
cadena = Pila()
operador = Operador()

while True: 
    print('1. Ingresar operacion')
    print('2. Salir')
    opcion = int(input('Ingrese una opción: '))

    if opcion == 1: 
        os.system ('cls')
        expresion = input('Ingrese una operación aritmética: ')

        # Se pide la expresión matemática y se recorre la cadena ingresada, se hace la comparación de que si en la expresion ingresada hay un operador
        # ese operador se guardará en la pila operador, el resto de la expresion se irá a la pila llamada pila
        for x in range(len(expresion)):
            operacion = expresion[x]
            if operacion == '^':
                operador.insertar(operacion)
            elif operacion == '*':
                operador.insertar(operacion)
            elif operacion == '/':
                operador.insertar(operacion)
            elif operacion == '+':
                operador.insertar(operacion)
            elif operacion == '-':
                operador.insertar(operacion)
            else:
                cadena.insertar(expresion[x])
        
        print('\nEl equivalente a notación postfija es: ')
        cadena.recorrer()
        operador.recorrer() 
        input('\n\nPresione cualquier tecla para continuar...')

    elif opcion == 2:
        break
    else:
        continue