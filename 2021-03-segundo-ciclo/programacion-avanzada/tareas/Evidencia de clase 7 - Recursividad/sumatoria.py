def sumatoria(n):
    if n == 1:
        return 1
    else:
        return n + sumatoria(n - 1)

# Bloque principal
numero = int(input('Ingrese el numero: '))
r = sumatoria(numero)
print(f"El resultado es: {r}")