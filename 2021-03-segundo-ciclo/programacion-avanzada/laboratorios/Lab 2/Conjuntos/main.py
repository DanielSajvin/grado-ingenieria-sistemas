from conjunto import Conjunto

print('\n----- CONJUNTOS -----\n')

conj_a = Conjunto('A')
conj_b = Conjunto('B')
conj_c = Conjunto('C')

while True: 
    print('1. Ingresar elementos al conjunto A')
    print('2. Ingresar elementos al conjunto B')
    print('3. Ingresar elementos al conjunto C')
    print('4. Mostrar todos los elementos')
    print('5. Eliminar elementos de un conjunto')
    print('6. Vaciar un conjunto')
    print('7. Salir')
    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        element = int(input('\nIngrese elemento: '))
        Conjunto.agregar_elemento(conj_a, element)
    
    elif opcion == 2:
        element = int(input('\nIngrese elemento: '))
        Conjunto.agregar_elemento(conj_b, element)
    
    elif opcion == 3:
        element = int(input('\nIgrese elemento: '))
        Conjunto.agregar_elemento(conj_c, element)
    
    elif opcion == 4:
        print(conj_a)
        print(conj_b)
        print(conj_c)
    
    elif opcion == 5:
        while True: 
            eliminado = int(input('\nIngrese el numero a eliminar: '))
            if eliminado >= 0:
                Conjunto.eliminar_elemento(conj_a, eliminado)
                Conjunto.eliminar_elemento(conj_b, eliminado)
                Conjunto.eliminar_elemento(conj_c, eliminado)
                break
            else:
                input('ERROR, INGRESE UN NUMERO IGUAL O MAYO A CERO')
                break
                continue
    
    elif opcion == 6:
        print('\nSeleccione un conjunto para eliminar su elementos: ')
        print('1. Conjunto A\n2. Conjunto B\n3. Conjunto C\n4. Volver al menú')
        vacio = int(input('¿Qué conjunto desea vaciar: '))

        if vacio == 1:
            Conjunto.vaciar_conj(conj_a)
            
        elif vacio == 2:
            Conjunto.vaciar_conj(conj_b)
           
        elif vacio == 3:
            Conjunto.vaciar_conj(conj_c)
            
        elif vacio == 4:
            break
        continue

    elif opcion == 7:
        break
    continue