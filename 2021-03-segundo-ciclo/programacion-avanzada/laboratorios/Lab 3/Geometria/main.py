from punto import Punto
from cmath import sqrt

coordenadas = []

print('\n--- Geometría ---\n')
print('A continuación debe ingresar la coordenada (x, y), solo deben ser número enteros.\n')
x = int(input('Ingrese la coordenada x: '))
y = int(input('Ingrese la coordenada y: '))
print('\nPara realizar una operación ingrese una nueva coordenada.\n')
x2 = int(input('Ingrese la coordenada x: '))
y2 = int(input('Ingrese la coordenada y: '))
ubi = Punto(x, y, x2, y2)
coordenadas.append(ubi)

# Parte donde se imprimen las coordenadas ingresadas
print(f"\nCoordenadas ingresadas: ({ubi.obtener_coordenada()}")

# Ciclo for para recorrer y averiguar el cuadrante en que se encuentra la primera coordenada ingresada
for x in coordenadas:
    print(f"\nEstá en el {x.obtener_cuadrante()}")

# Ciclo for para recorrer y averiguar el cuadrante resultante entre las dos distancias ingresadas
for x in coordenadas:
    print(f"\nCuadrante resultante: {x.vector_resultante()}")

# Parte donde se imprime la distancia entre las coordenadas ingresadas
print(f"\nLa distancia entre los dos puntos es: {ubi.disctancia_puntos()}")