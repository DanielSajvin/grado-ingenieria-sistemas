from persona import Persona

#
nombre = input('Ingrese nombre: ')
edad = int(input('Ingrese edad: '))
capital = float(input('Ingrese el capital: '))
peso = float(input('Ingrese peso (lb): '))
estatura = int(input('Ingrese la estatura (cm): '))

#Crear objeto
estudiante = Persona(nombre, edad, capital, peso, estatura)

#Mostrar resultados
es_mayor = estudiante.es_mayor_edad()
if es_mayor:
    print('\nEl estudiante es mayor de edad.')
else:
    print('\nEl estudiante es menor de edad.')

imc = estudiante.calcular_IMC()
print(f"\nEl indice de masa corporal es: {imc}")

composicion = estudiante.obtener_composicion_corporal()
print(f"La composición corporal es: {composicion}")

capital_final = estudiante.calcular_capital_final(0.05, 20)
print(f"\nEl capital final es: Q.{capital_final}")
