def potencias(num1, num2):
    if num2 == 0:
        return 1
    else:
        potencia = num1 * potencias(num1, num2 - 1)
    return potencia

num1 = int(input('Ingrese un numero entero: '))
num2 = int(input('Ingrese un numero entero: '))
r = potencias(num1, num2)
print(f"La potencia es: {r}")