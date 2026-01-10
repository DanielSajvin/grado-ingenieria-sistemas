from lista import Lista
import os

print('---   ROTAR CANCIONES   ---\n')
canciones = Lista()

while True:
    os.system('cls')
    print('MENÚ\n')
    print('1. Ingresar canción')
    print('2. Quitar canción')
    print('3. Mover hacia adelante')
    print('4. Mover hacia atrás')
    print('5. Salir')
    opcion = int(input('Seleccione una opción: '))

    if opcion == 1:
        os.system('cls')
        print('INGRESAR CANCIONES: \n')
        cancion_n = input('Ingrese el nombre de la canción: ')
        artista_n = input('Ingrese el nombre del artista: ')
        canciones.insertar_final(cancion_n, artista_n)
        print(canciones.recorrer())
        os.system('pause')
    elif opcion == 2:
        os.system('cls')
        print('QUITAR UNA CANCIÓN: \n')
        elim1 = input('Ingrese el nombre de la canción que desea eliminar: ')
        elim2 = input('Ingrese el nombre del artista: ')
        canciones.eliminar_referencia(elim1, elim2)
        print(canciones.recorrer())
        os.system('pause')
    elif opcion == 3:
        os.system('cls')
        print('ACTUALIZAR CANCIONES: \n')
        canciones.mover_adelante()
        print(canciones.recorrer())
        os.system('pause')
    elif opcion == 4:
        os.system('cls')
        print('ACTUALIZAR CANCIONES: ')
        canciones.mover_adelante()
        print(canciones.recorrer())
        os.system('pause')
    elif opcion == 5:
        break
    else:
        continue    