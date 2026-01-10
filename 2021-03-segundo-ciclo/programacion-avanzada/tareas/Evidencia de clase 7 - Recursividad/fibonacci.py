def fibonacci(n):
    # Paso base 1
    if n == 0:
        return 0 
    
    # Paso base 2
    elif n == 1:
        return 1
    else:
        # Paso recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)

# Bloque principal
numero = int(input('Ingrese un número: '))
r = fibonacci(numero)
print(f"El resultado es: {r}")