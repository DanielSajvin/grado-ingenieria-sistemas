from peliculas import Pelicula
from os import system

print('-----  REPRODUCTOR DE PELICULAS  -----')

peliculas = []

while True:
    print('MENU')
    print('1. Ingresar nueva película')
    print('2. Marcar cancion como favorita')
    print('3. Ver todas las canciones')
    print('4. Salir')
    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        system('cls')
        peli = input('Ingrese el nombre de la pelicula: ')
        tiempo = int(input('Ingrese la duración de la película en segundos: '))
        cnom = input('Ingrese el nombre del estudio cinematográfico: ')
        cpais = input('Ingrese el país del estudi cinematográfico: ')
        pelicula = Pelicula(peli, tiempo, cnom, cpais)
        peliculas.append(pelicula)
        input('Presione cualquier tecla para continuar...')
    elif opcion == 2:
        system('cls')
        encontrado = False
        npeli = input('Ingrese el nombre de la pelicula que desea hacer favorita: ')
        estudio = input('Ingrese el nombre del estudio de la película: ')
        for x in peliculas:
            if Pelicula.nombre_pelicula(x) == npeli and Pelicula.estudio(x) == estudio:
                x.favorita()
                encontrado = True
                break
        
        if encontrado == True:
            print('Película encontrada.')
        else:
            print('No se encontró la película.')
        input('Presione cualquier tecla para continuar...')
    elif opcion == 3:
        system('cls')
        for x in peliculas:
            print(x)
        input('Presione cualquier tecla para continuar...')
    elif opcion == 4:
        break
    else:
        continue