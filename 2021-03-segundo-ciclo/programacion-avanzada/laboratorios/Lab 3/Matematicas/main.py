from calculo import Calculo

print('--- MATEMATICAS ---')

numero = int(input('\nIngrese un número entero: '))

calc = Calculo(numero)

# Llamar al metodo para que imprima el resultado
resultado1 = calc.calcular_factorial()
print(f"\nEl factorial del número es: {resultado1}")

# Como se recibe un bool se hace la condicion para que imprima en pantalla
resultado2 = calc.es_primo()
if resultado2:
    print('\nEl número es primo\n')
else:
    print('\nEl numero es compuesto\n')

# LLamando al metodo a ejecutarse 
calc.obtener_tabla_multiplicar()

# LLamando al metodo a ejecutarse 
calc.obtener_divisibles()