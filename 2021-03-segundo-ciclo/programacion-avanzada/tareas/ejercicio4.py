# Operadores aritméticos 
numero = 1 +2 * 3 / 4
print(numero)

# Para transformar de float a int
resultado = int(numero) 
print(resultado)

# Para aproximar 
aproximacion = round(2.3333, 0)
aproximacion2 = round(2.3333, 2)
aproximacion3 = round(2.8, 0)

print('Aproximaciones: ')
print(aproximacion)
print(aproximacion2)
print(aproximacion3)

mensaje1 = "Hola"
mensaje2 = " Mundo"

mensaje_resultado = mensaje1 + mensaje2
print(mensaje_resultado)
print(" ")
mensaje_resultado1 = f"{mensaje1} {mensaje2}"
print(mensaje_resultado1)
mensaje_resultado2 = (mensaje1 + "\n") * 5
print(mensaje_resultado2)