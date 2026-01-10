def obtener_numero(fila, columna):
    if fila == 0:
        return 1
    elif columna == 0:
        return 1
    elif fila == columna:
        return 1
    else:
        a = obtener_numero(fila - 1, columna - 1)
        b = obtener_numero(fila - 1, columna)
        resultado = a + b
        return resultado 

def triangulo_pascal(nivel, columna):
    if nivel == columna:
        numero = obtener_numero(nivel, columna) # Devuelve un entero 
        return str(numero)
    else:
        amarillo = str(obtener_numero(nivel, columna))
        verde = triangulo_pascal(nivel, columna + 1) # Devuelve un str
        return amarillo + "-" + verde

def obtener_triangulo(nivel):
    if nivel == 0:
        return triangulo_pascal(0, 0)
    else:
        amarillo = triangulo_pascal(nivel, 0)
        verde = obtener_triangulo(nivel - 1)
        return verde + "\n" + amarillo
       
# Bloque principal
nivel = int(input('Ingrese el nivel: '))
r = obtener_triangulo(nivel)
print(r)