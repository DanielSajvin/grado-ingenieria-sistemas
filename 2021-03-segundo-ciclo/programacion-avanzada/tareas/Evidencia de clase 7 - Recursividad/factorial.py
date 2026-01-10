def factorial(n):
    resultado = 0
    #Paso base no depende de otros calculos
    if n == 1 or n == 2:
        resultado = n
    #Depende de otros calculos (Paso recursivo)
    else:
        resultado = n * factorial(n - 1)
    return resultado

#Bloque principal
numero = int(input('Ingrese un número: '))
resultado = factorial(numero)

print(f"El resultado es: {resultado}")