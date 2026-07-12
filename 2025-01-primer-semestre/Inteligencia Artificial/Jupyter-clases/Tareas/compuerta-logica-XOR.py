import random

# Parámetro de tasa de aprendizaje
learning_rate = 0.1

# Datos de entrenamiento para XOR con una nueva característica x3 = x1 * x2
inputs = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]] # esto porque un perceptron no puede resolver el problema de XOR, ya que no es linealmente separable
expected_outputs = [0, 1, 1, 0]

# Inicializar pesos aleatorios
weights = [random.random(), random.random(), random.random(), random.random()]

epochs = 10000

for epoch in range(epochs):
    has_error = False
    for i in range(4):
        x1, x2, x3 = inputs[i]
        expected = expected_outputs[i]

        # Cálculo de la salida del perceptrón con función de activación escalón
        sum_value = x1 * weights[0] + x2 * weights[1] + x3 * weights[2] + weights[3]
        output = 1 if sum_value > 0 else 0

        # Calcular error
        error = expected - output
        if error != 0:
            has_error = True
            # Ajustar pesos
            weights[0] += learning_rate * error * x1
            weights[1] += learning_rate * error * x2
            weights[2] += learning_rate * error * x3
            weights[3] += learning_rate * error  # Sesgo

    if not has_error:
        print(f"Entrenamiento finalizado en la época {epoch}")
        break

print("\nResultados finales:")
for i in range(4):
    x1, x2, x3 = inputs[i]
    sum_value = x1 * weights[0] + x2 * weights[1] + x3 * weights[2] + weights[3]
    output = 1 if sum_value > 0 else 0
    print(f"Entrada: {x1} XOR {x2} = {output} (Esperado: {expected_outputs[i]})")
