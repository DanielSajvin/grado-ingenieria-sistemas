import random
import heapq
import numpy as np

## Solución horario de 16:00 a 21:00

# Configuración parametrizable
TIEMPO_SIMULACION = 300  # en minutos

# Llegadas (Source, Exponential)
EXPO_LOCATION = 0
EXPO_SCALE = 0.283

# Porcentaje a cajas asistidas vs autopago
PORCENTAJE_ASISTIDAS = 0.45  # 45% asistidas, 55% autopago

# Cajas asistidas, lognormal
NUM_CAJAS_ASISTIDAS = 4 
LOGN_LOCATION = 0
LOGN_MEAN = 0.581
LOGN_STD = 0.4725

# Cajas autopago, triangular
NUM_CAJAS_AUTOPAGO = 4 
TRI_MIN = 0.75
TRI_MAX = 5
TRI_MODE = 1.6



# Estructuras y eventos

class Cliente:
    def __init__(self, tiempo_llegada):
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_inicio = None
        self.tiempo_fin = None


class Caja:
    def __init__(self, tipo, id):
        self.tipo = tipo  # 'asistida' o 'autopago'
        self.id = id
        self.cola = []
        self.tiempo_ocupado = 0
        self.tiempo_libre = 0
        self.clientes_atendidos = []
        self.ocupada = False
        self.proximo_libre = 0

    def tiempo_proceso(self):
        if self.tipo == "asistida":
            return max(0, np.random.lognormal(LOGN_MEAN, LOGN_STD)) + LOGN_LOCATION
        else:
            return random.triangular(TRI_MIN, TRI_MAX, TRI_MODE)

    def asignar_cliente(self, cliente, ahora):
        inicio = max(ahora, self.proximo_libre)
        duracion = self.tiempo_proceso()
        fin = inicio + duracion

        cliente.tiempo_inicio = inicio
        cliente.tiempo_fin = fin
        self.proximo_libre = fin
        self.tiempo_ocupado += duracion
        self.clientes_atendidos.append(cliente)
        return fin



# Simulación

def simular():
    # Crear cajas
    cajas_asistidas = [Caja("asistida", i) for i in range(NUM_CAJAS_ASISTIDAS)]
    cajas_autopago = [Caja("autopago", i) for i in range(NUM_CAJAS_AUTOPAGO)]

    eventos = []
    tiempo = 0

    # Generar clientes
    while tiempo < TIEMPO_SIMULACION:
        llegada = EXPO_LOCATION + np.random.exponential(EXPO_SCALE)
        tiempo += llegada
        if tiempo > TIEMPO_SIMULACION:
            break

        cliente = Cliente(tiempo)

        if random.random() < PORCENTAJE_ASISTIDAS:
            cola = cajas_asistidas
        else:
            cola = cajas_autopago

        # Caja con la cola más corta disponible
        caja = min(
            cola,
            key=lambda c: len(
                [cli for cli in c.clientes_atendidos if cli.tiempo_fin > tiempo]
            ),
        )
        fin = caja.asignar_cliente(cliente, tiempo)
        heapq.heappush(eventos, (fin, cliente))

    # Resultados
    print("\nResultados de la simulación:\n")
    for grupo, cajas in [
        ("Cajas Asistidas", cajas_asistidas),
        ("Cajas Autopago", cajas_autopago),
    ]:
        print(f"--- {grupo} ---")
        for caja in cajas:
            clientes = caja.clientes_atendidos
            esperas = [c.tiempo_inicio - c.tiempo_llegada for c in clientes]
            max_espera = max(esperas) if esperas else 0
            promedio_espera = sum(esperas) / len(esperas) if esperas else 0
            tiempo_libre = TIEMPO_SIMULACION - caja.tiempo_ocupado

            print(f"Caja {caja.id}:")
            print(f"  Clientes atendidos: {len(clientes)}")
            print(f"  Tiempo libre: {tiempo_libre:.2f} min")
            print(f"  Tiempo promedio de espera: {promedio_espera:.2f} min")
            print(f"  Tiempo máximo de espera: {max_espera:.2f} min")
            print("")


if __name__ == "__main__":
    simular()
