print("--- Números perfectos ---\n")
print("Instrucciones: ")
print("Debe ingresar un número entero, el programa le dirá si ese número es")
print("un número perfecto, abundante o deficiente. \n")
# En esta parte el ususario debe ingresar un numero entero 
print("Ingresar número entero: ")
num = int(input())
# En esta parte declaramos estas variables con un valor de 0 ya que me va a ayudar en el ciclo siguiente 
f = 0
sum = 0
i = 0
# Acá le estoy diciendo al ciclo que va a iniciar en 0 y va a llegar hasta el valor que ingrese el usuario, se le resta 1 ya que 
# inicia en 0 y no en 1
while i < (num -1):
 # Acá estoy sacando el MOD del número ingresado, por ejemplo si es 5 le va sacar MOD a 1, 2, 3, hasta llegar a 5 y solo va a tomar
 # en cuenta los que den 0
    if (num % (i + 1)) == 0:
        f = i + 1
        # Sum inicia en 0 y se le suma f que vienen siendo los factores
        sum = sum + f
    i = i + 1 
# Acá se hace una condicion que si sum es igual al numero ingresado pues es perfecto  
if sum == num:
    print(f"{num} es un número perfecto.")
# Si sum es mayor al número ingresado es abundante 
elif sum > num:
    print(f"{num} es un número abundante.")
# Si sum es menor al número ingresado es deficiente 
elif sum < num:
    print(f"{num} es un número deficiente.")