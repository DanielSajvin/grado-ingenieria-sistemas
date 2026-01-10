from canciones import Cancion
from os import system

print('-----  REPRODUCTOR DE CANCIONES  -----')

canciones = []

while True:
    print('MENU')
    print('1. Ingresar nueva cancion')
    print('2. Marcar cancion como favorita')
    print('3. Ver todas las canciones')
    print('4. Salir')
    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        system('cls')
        canc = input('Ingrese el nombre de la canción: ')
        nomb = input('Ingrese el del artista: ')
        fecha = input('Ingrese la fecha: ') # la fecha se ingresa 10/20/45
        cancion = Cancion(canc, nomb, fecha)
        canciones.append(cancion)
        input('Presione cualquier tecla para continuar...')
    elif opcion == 2:
        system('cls')
        encontrado = False
        song = input('Ingrese el nombre de la canción que desea hacer favorita: ')
        artist = input('Ingrese el nombre del artista de la canción: ')
        for x in canciones:
            if Cancion.nombre_cancion(x) == song and Cancion.artista(x) == artist:
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
        for x in canciones:
            print(x)
        input('Presione cualquier tecla para continuar...')
    elif opcion == 4:
        break
    else:
        continue