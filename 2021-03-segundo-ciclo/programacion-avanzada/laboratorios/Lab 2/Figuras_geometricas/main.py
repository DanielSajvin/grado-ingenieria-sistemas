from circulo import Circulo
from triangulo import Triangulo
from cuadrado import Cuadrado

print('\n ----- AREA FIGURAS GEOMETRICAS -----\n')

while True:
    print('1.  Calcular área de un triángulo rectángulo')
    print('2.  Calcular área de un cuadrado')
    print('3.  Calcular área de un círculo')
    print('4.  Salir')
    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        h = float(input('\nIngrese la altura: '))
        b = float(input('Ingrese la base: '))

        altura12 = Triangulo(h, b)

    elif opcion == 2:
        l1 = float(input('\nIngrese un lado: '))
        cuad = Cuadrado(l1)

    elif opcion == 3:
        c1 = float(input('\nIngrese el radio: '))
        cir = Circulo(c1)
    
    elif opcion == 4:
        break
    continue