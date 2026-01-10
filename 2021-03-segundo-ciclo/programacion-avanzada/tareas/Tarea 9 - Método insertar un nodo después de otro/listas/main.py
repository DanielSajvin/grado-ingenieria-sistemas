from lista import Lista
 
# Bloque principal 
estudiantes = Lista()
print('PRIMER PASO')
print(estudiantes)
print('Elementos: ' + estudiantes.recorrer())

estudiantes.insertar_inicio('Daniela')
estudiantes.insertar_inicio('Allan')
estudiantes.insertar_inicio('Rodrigo')

print('\nPASOS DE 2 - 4')
print(estudiantes)
print('Elementos: ' + estudiantes.recorrer())

estudiantes.insertar_final('Diego')
estudiantes.insertar_final('Ruben')
estudiantes.insertar_final('Karla')
estudiantes.insertar_final('Gerardo')

print('\nPASOS DE 5 - 7')
print(estudiantes)
print('Elementos: ' + estudiantes.recorrer())

nodo = estudiantes.buscar_nodo_valor('Daniela')
print('\nPASO 8')
print(nodo)

nodo = estudiantes.buscar_nodo_valor('Ruben')
print('\nPASO 9')
print(nodo)

nodo = estudiantes.buscar_nodo_posicion(2)
print('\nPASO 10')
print(nodo)

nodo = estudiantes.buscar_nodo_posicion(4)
print('\nPASO 11')
print(nodo)

posicion = estudiantes.buscar_posicion_nodo('Daniela')
print('\nPASO 12')
print('La posición es: ', posicion)

posicion = estudiantes.buscar_posicion_nodo('Ruben')
print('\nPASO 13')
print('La posición es: ', posicion)

estudiantes.insertar_antes('Pablo', 'Diego')
print('\nPASO 14')
print(estudiantes.recorrer())

# Inserta en el medio digamos de la lista
estudiantes.insertar_despues('Daniel', 'Allan')
print('\nPASO 15')
print(estudiantes.recorrer())

estudiantes.insertar_despues('Mario', 'Diego')
print('\nPASO 16')
print(estudiantes.recorrer())

# Insertar depues, si ya no existe "depues" es decir que, se quiere insertar depues del ultimo elemento de la lista
estudiantes.insertar_despues('David', 'Gerardo')
print('\nPASO 17')
print(estudiantes.recorrer())