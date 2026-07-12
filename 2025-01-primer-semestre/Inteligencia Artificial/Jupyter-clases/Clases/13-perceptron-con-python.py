import random

# Conjunto de datos para entrenamiento de la puerta AND
datos = [[1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 0]]

# Inicialización de pesos y umbral con valores aleatorios
pesos = [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)]

# Fase de aprendizaje
aprendizaje = True
epocas = 0

while aprendizaje:
    aprendizaje = False
    for i in range(4):
        salida_doub = datos[i][0] * pesos[0] + datos[i][1] * pesos[1] + pesos[2]
        salida_int = 1 if salida_doub > 0 else 0
        
        if salida_int != datos[i][2]:  # Si la salida no coincide con el dato esperado
            pesos[0] = random.uniform(-1, 1)
            pesos[1] = random.uniform(-1, 1)
            pesos[2] = random.uniform(-1, 1)
            aprendizaje = True
    epocas += 1

# Fase de verificación de resultados
print("\nResultados del perceptrón:")
for i in range(4):
    salida_doub = datos[i][0] * pesos[0] + datos[i][1] * pesos[1] + pesos[2]
    salida_int = 1 if salida_doub > 0 else 0
    print(f"Entradas: {datos[i][0]} AND {datos[i][1]} = {datos[i][2]} | Perceptron: {salida_int}")

print(f"\nÉpocas: {epocas}")
print(f"Pesos finales: p0 = {pesos[0]:.4f}, p1 = {pesos[1]:.4f}, Umbral (bias) = {pesos[2]:.4f}")

# Mantener la ventana abierta (opcional)
input("\nPresiona Enter para salir...")
