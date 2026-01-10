from pila import Pila

# Bloque principal
# 1. Crear una pila de peliculas disponibles
peliculas_disponibles = Pila()

print('Primer paso')
print(peliculas_disponibles.tamaño)
print(peliculas_disponibles.tope)

# 2.  Insertar Venom 2 
peliculas_disponibles.insertar('Venom 2')

print('Segundo paso')
print(peliculas_disponibles.tamaño)
print(peliculas_disponibles.tope)

# 3. Insertar Paw patrol la pelicula
peliculas_disponibles.insertar('Paw Patrol: La Película')

print('Tercer paso')
print(peliculas_disponibles.tamaño)
print(peliculas_disponibles.tope)
print(peliculas_disponibles.tope.siguiente)

# 4. Insertar Sin tiempo para morir
peliculas_disponibles.insertar('Sin tiempo para morir')

print('Cuarto paso')
print(peliculas_disponibles.tamaño)
print(peliculas_disponibles.tope)
print(peliculas_disponibles.tope.siguiente)
print(peliculas_disponibles.tope.siguiente.siguiente)
print(peliculas_disponibles.tope.siguiente.siguiente.siguiente)

# 5. Recorrer la pila de películas disponibles
print('Quinto paso')
peliculas_disponibles.recorrer()

# 6. Crear pila de próximos estrenos (max: 3)
proximos_estrenos = Pila(3)
print('Sexto Paso')
print(proximos_estrenos.tamaño)
print(proximos_estrenos.tope)
print(proximos_estrenos.max)

try:

    proximos_estrenos.insertar('Spiderman')
    proximos_estrenos.insertar('Hallowen')
    proximos_estrenos.insertar('Misión imposible')
    #proximos_estrenos.insertar('Mi pobre angelito')
except Exception as error:
    print('Ocurrió un error al insertar')
    print(error)

print(proximos_estrenos.tamaño)

# 11. Eliminar en peliculas disponibles
peliculas_disponibles.eliminar()
print('Paso 11')
print(peliculas_disponibles.tamaño)

# 12 Eliminar en peliculas disponibles
peliculas_disponibles.eliminar()
print('Paso 12')
print(peliculas_disponibles.tamaño)

# 13 Eliminar en peliculas disponibles
peliculas_disponibles.eliminar()
print('Paso 13')
print(peliculas_disponibles.tamaño)

# 14 Eliminar en peliculas disponibles
try: 
    peliculas_disponibles.eliminar()
    print('Paso 14')
    print(peliculas_disponibles.tamaño)
except Exception as error:
    print(error)