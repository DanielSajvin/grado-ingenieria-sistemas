from pila import Pila
import os

print('-----   INSERCCIÓN CONTROLADA   -----\n')
libro = Pila()

while True:
    os.system ('cls')
    print('1. Ingresar un libro')
    print('2. Ver tamaño de pila')
    print('3. Mostrar todos los libros')
    print('4. Salir')
    opcion = int(input('Ingrese una opción: '))
    if opcion == 1:
        os.system ('cls')
        try: 
            nombre = input('Ingrese el nombre del libro: ')
            editorial = input('Ingrese la editorial del libro: ')
            isbn = int(input('Ingrese el ISBN del libro: '))
            libro.insertar(nombre, editorial, isbn)
        except Exception as error:
            print(f"Ocurrió un error al insertar: {error}")
        input('Presione cualquier tecla para continuar...')
    elif opcion == 2:
        os.system ('cls')
        print(libro.tamaño)
        input('Presione cualquier tecla para continuar...')
    elif opcion == 3:
        os.system ('cls')
        libro.recorrer()
        input('Presione cualquier tecla para continuar...')
    elif opcion == 4:
        break 
    else: 
        continue