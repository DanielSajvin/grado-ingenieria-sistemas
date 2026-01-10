print("--- Bienvenido al conversor de unidades ---\n")
print("Ingrese el número 1 si desea convertir libras a kilogramos")
print("Ingrese el número 2 si desea convertir metros a kilómetros")
print("Ingrese el número 3 si desea convertir litros a galones")

# Se le pide al usuario que elige una de las tres opciones 
print("Que desea realizar: ")
opcion = int(input())

# Dependiendo de la opcion que eliga, hará la acción que corresponda a esa opción
if opcion == 1:
    print("Ingrese la cantidad que en libras: ")
    lbrs = float(input())
    kg = lbrs / 2.205
    print(f"{lbrs} libras equivale a {kg} kilogramos")
elif opcion == 2:
    print("Ingrese la cantidad que en metros: ")
    mts = float(input())
    km = mts / 1000
    print(f"{mts} metros equivale a {km} kilómetros")
elif opcion == 3:
    print("Ingrese la cantidad que en litros: ")
    lt = float(input())
    gal = lt / 3.785
    print(f"{lt} litros equivale a {gal} galones")
# Si el usuario ingresa otro numero que no sea 1, 2 o 3 que son las opciones a elegir, le mostrará este mensaje de error
else:
    print("OPCION INVALIDA SELECCIONES 1 DE LAS 3 DISPONIBLES")