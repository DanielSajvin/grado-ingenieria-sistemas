print("--- Encuentra el numero menor y mayor ---\n")
print("Instrucciones:")
print("A continuación se le pedirá que ingrese 5 número enteros,")
print("el programa le mostrará el número mayor y menor de los que ingresó.\n")
# En esta parte se le pide al usuario que ingrese una serie de números enteros
print("Ingrese No. 1: ")
num1 = int(input())
print("Ingrese No. 2: ")
num2 = int(input())
print("Ingrese No. 3: ")
num3 = int(input())
print("Ingrese No. 4: ")
num4 = int(input())
print("Ingrese No. 5: ")
num5 = int(input())
# La función MAX sirve para detectar el número mayor dentro de una serie de números, de esta forma es como se va a encontrar
# el número mayor dentro de la serie de número que ingresó el usuario
mayor = max(num1, num2, num3, num4, num5)
# La función MIN de igual forma sirve para encontrar el número menor dentro de una serie de números, de igual forma así
# es como va a buscar dentro de los 5 números que ingresó el usuario cual es el menor
menor = min(num1, num2, num3, num4, num5)
# En esta parte ya solo se le indica al usuario cual es el número mayor y cual es el menor de los 5 que ingresó 
print(f"El número mayor es {mayor} y el número menor es {menor}")