from pynput import mouse
import time

# Lista para guardar posiciones del mouse
posiciones = []


def on_move(x, y):
    posiciones.append((x, y))


def capturar_movimiento(tiempo=5):
    print(f"\nPASO 1: Captura de movimiento del mouse")
    print(f"Mueve el mouse libremente durante {tiempo} segundos...")
    with mouse.Listener(on_move=on_move) as listener:
        time.sleep(tiempo)
        listener.stop()
    print(f"Se capturaron {len(posiciones)} posiciones del mouse.")


def mostrar_muestras():
    print(
        "\nMuestra de algunas posiciones capturadas:"
    )  # solo se muestran 5 posiciones
    for i, (x, y) in enumerate(posiciones[:5]):
        print(f"  Posición {i+1}: x = {x}, y = {y}")
    if len(posiciones) > 5:
        print(f"  ... y {len(posiciones) - 5} más.")


def generar_semilla(digitos):
    print("\nPASO 2: Generación de la semilla")
    if not posiciones:
        raise ValueError("No se capturaron posiciones del mouse.")

    suma_total = 0
    print("Calculando la semilla como suma de x * y para cada posición capturada...")

    for i, (x, y) in enumerate(posiciones):
        producto = x * y
        suma_total += producto
        if i < 5:  # solo se muestran los primeros 5 calculos
            print(
                f"   x = {x}, y = {y}, x*y = {producto}, suma acumulada = {suma_total}"
            )

    semilla_cruda = abs(suma_total)
    semilla_str = str(semilla_cruda).replace("-", "")
    semilla_final = int(semilla_str) % (10**digitos)

    print(f"Suma total = {suma_total}")
    print(f"Semilla cruda = {semilla_str}")
    print(f"Semilla final (reducida a {digitos} dígitos): {semilla_final}")

    return semilla_final


def cuadrado_medio(semilla, n_digitos=4, iteraciones=10):
    resultados = []
    x = semilla
    print(f"\nPASO 3: Generación de números con el método del cuadrado medio")
    for i in range(iteraciones):
        cuadrado = str(x**2).zfill(2 * n_digitos)
        mitad = len(cuadrado) // 2
        nuevo = int(cuadrado[mitad - n_digitos // 2 : mitad + n_digitos // 2])
        resultados.append(nuevo)

        print(f"\nIteración {i+1}")
        print(f"   Semilla actual: {x}")
        print(f"   Cuadrado: {x}^2 = {x**2}")
        print(f"   Cuadrado con ceros (relleno): {cuadrado}")
        print(f"   Extrayendo los {n_digitos} dígitos del centro -> {nuevo}")

        x = nuevo
    return resultados


try:
    print("Generador de números pseudoaleatorios usando el método del cuadrado medio\n")

    n_digitos = int(input("¿De cuántos dígitos debe ser la semilla?: "))
    if n_digitos < 2 or n_digitos > 10:
        raise ValueError("El número de dígitos debe estar entre 2 y 10.")

    n_numeros = int(input("¿Cuántos números pseudoaleatorios deseas generar?: "))

    capturar_movimiento()
    mostrar_muestras()

    semilla = generar_semilla(n_digitos)

    numeros = cuadrado_medio(semilla, n_digitos, n_numeros)

    print("\nRESULTADO FINAL:")
    print("Números pseudoaleatorios generados:", numeros)

except Exception as e:
    print(f"Error: {e}")

54598606