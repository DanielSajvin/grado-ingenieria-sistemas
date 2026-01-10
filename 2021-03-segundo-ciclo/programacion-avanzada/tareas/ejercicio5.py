# Operaciones logicas AND, OR, NOT, 
# IGUAL, NO ES IGUAL, MENOR Y MAYOR, MAYOR Y MENOR IGUAL
# Condiciones

x = 65
x == 65
print(x == 65)
print(x < 65)
print(x > 65)
print(x <= 65)
print(x >= 65)
print(x != 65)

if x >= 65:
    print("GANO EL CURSO")
elif x <= 35 & x < 65:
    print("PERDIO EL CURSO :'(")
else:
    print("Usted no tiene derecho a evaluacion")
