print("--- Calculador de impuestos ---\n")
# Se le dan las instrucciones al usuario sobre el funcionamiento del programa
print("Instrucciones: ")
print("Ingrese el precio de la calculadora, seguidamente")
print("ingrese la cantidad de unidades vendidas.\n")
# Se le pide que ingrese el precio al usuario 
print("Ingresar precio: ")
precio = float(input())
# Si el usuario llega a ingresar 0 o un número menor a cero se le mostrará este mensaje de error, ya que ningún producto
# puede valer Q.0.00
if precio <= 0:
    print("ERROR! EL PRECIO NO PUEDE SER MENOR O IGUAL A 0")
# Si ingresa un valor mayor a cero el programa continua, pidiendo los datos que en este caso con las unidades vendidas
else :
    print("Ingresar cantidad de unidades vendidas: ")
    vendido = int(input())
# Acá se vuelve a validar que el usuario ingrese una cantidad correcta, ya que si ingresa 0 o un número menor a 0 
# pues da error ya no puede no haber vendido nada, si es el caso pues entonces en teoria no deberia pagar impuestos
if vendido <= 0:
    print("ERROR! NO PUEDE VENDER 0 O MENOS DE 0 UNIDADES")
# Bueno ya validando todo y que marche todo bien, se multiplican el precio y las unidades vendidas ya que de esa forma 
# se puede averiguar cuanto en dinero es lo que se vendió
else :
    total = precio * vendido
# A contiuación se hace una comparación, si la operación anterior da un valor mayor o igual a 10000 pues deberá pagar el 19%
if total >= 10000:
    resultado1 = total * 0.19
    print(f"El total de impuestos a pagar es Q.{resultado1}")
# De lo contrario si el valor anterior es menor a 10000 pues solo pagará el 5%
elif total < 10000:
    resultado2 = total *0.05
    print(f"El total de impuestos a pagar es Q.{resultado2}")