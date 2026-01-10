import math

print('--- CALCULAR CUADRATICA ---\n')
x1 = 0
x2 = 0
try:
    a = int(input('Ingrese el número a: '))
    b = int(input('Ingrese el número b: '))
    c = int(input('Ingrese el número c: '))

    x1 = (-b + math.sqrt((b*b)-4*a*c)) / 2*a
    x2 = (-b - math.sqrt((b*b)-4*a*c)) / 2*a
except ZeroDivisionError: # Por si el denominador es 0 
    print('¡¡Los ceros no pueden dividir!!')
except ValueError:# Por si el usuario ingresa una letra o cualquier cosa en vez de un número o por si queda una raíz negativa
    print('No se pueden operar solociones no reales o puede que no esté ingreando números.')
else:
    print(f"X1 es: {x1}\nX2 es: {x2}")