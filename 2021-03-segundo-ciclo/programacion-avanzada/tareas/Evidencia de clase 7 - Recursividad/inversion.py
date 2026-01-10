#def inversion(n):
#    if n == 0:
#        return 1000
#    else:
#        return inversion(n - 1) + (inversion(n - 1) * 0.1)

#año = int(input('Ingrese el número de años: '))
#r = inversion(año)
#print(r)

def calcular_monto(años, monto, interes):
    if años == 0:
        return monto
    elif años == 1:
        capital = calcular_monto(0, monto, interes)
        interes_ganado = capital * interes
        return capital + interes_ganado
    elif años == 2:
        capital = calcular_monto(1, monto, interes)
        interes_ganado = capital * interes
        return capital + interes_ganado
    elif años == 3:
        capital = calcular_monto(2, monto, interes)
        interes_ganado = capital * interes
        return capital + interes_ganado
    else:
        capital = calcular_monto(años - 1, monto, interes)
        interes_ganado = capital * interes
        return capital + interes_ganado


# Bloque principal
monto = float(input('Ingrese el monto inicial: '))
años = int(input('Ingrese los años de ahorro: '))
interes = float(input('Ingrese la tasa de interes: '))
r = calcular_monto(años, monto, interes)
print(f"Usted tiene en el banco: Q.{r}")