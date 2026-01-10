def euclides(a, b):
    if b == 0:
        return f"MCD{a, b} = {a}"
    else: 
        res = a % b
        return euclides(b, res)

# Bloque principal
a = int(input('Ingrese un número entero: '))
b = int(input('Ingrese un número entero: '))

if b > a: 
    c = a
    a = b
    b = c

r = euclides(a, b)
print(r)