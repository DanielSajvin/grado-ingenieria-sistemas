import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Tiempos de espera en cada universidad
tiempos_espera = {
    "A": 0.0,  # USAC
    "B": 0.9,  # URL
    "C": 1.4,  # UVG
    "D": 1.1,  # UMG
    "E": 0.7,  # Mesoamericana
    "F": 1.3,  # USPG
    "G": 0.6,  # Galileo
    "H": 1.0,  # UPANA
    "I": 1.2,  # Da Vinci
    "J": 0.9,  # InterNaciones
    "K": 1.0,  # Universidad Regional
    "L": 1.6,  # Universidad Rural (Destino final)
}

# Grafo con tiempos de viaje (aristas)
grafo = {
    "A": {"B": 0.5, "G": 0.4, "H": 0.8, "I": 1.0},
    "B": {"C": 0.6, "I": 1.1},
    "G": {"C": 0.7, "D": 0.9},
    "C": {"D": 1.0, "H": 0.6, "I": 0.8},
    "D": {"E": 1.0, "I": 0.5},
    "I": {"E": 0.9, "J": 0.7},
    "E": {"F": 1.0, "J": 0.6},
    "J": {"K": 0.5, "L": 1.0},
    "K": {"F": 0.9, "L": 1.0},
    "F": {"L": 0.8},
}


# Algoritmo de Dijkstra que devuelve múltiples rutas
def dijkstra_con_rutas(grafo, tiempos_espera, inicio, destino, max_rutas=3):
    heap = [(0, inicio, [])]
    rutas = []

    while heap and len(rutas) < max_rutas:
        tiempo_actual, nodo_actual, camino = heapq.heappop(heap)
        camino = camino + [nodo_actual]

        if nodo_actual == destino:
            rutas.append((tiempo_actual, camino))
            continue

        for vecino, tiempo_viaje in grafo.get(nodo_actual, {}).items():
            if vecino not in camino:
                tiempo_total = tiempo_actual + tiempo_viaje + tiempos_espera[vecino]
                heapq.heappush(heap, (tiempo_total, vecino, camino))

    return rutas


# Calcular desglose de tiempos
def desglose_tiempos(camino):
    tiempo_viaje = 0
    tiempo_espera_total = 0
    for i in range(len(camino) - 1):
        tiempo_viaje += grafo[camino[i]][camino[i + 1]]
    for nodo in camino[1:]:  # no contar espera en nodo inicial
        tiempo_espera_total += tiempos_espera[nodo]
    return tiempo_viaje, tiempo_espera_total


# Obtener rutas
rutas = dijkstra_con_rutas(grafo, tiempos_espera, "A", "L", max_rutas=10)
rutas_unicas = []
usadas = set()

# Filtrar 3 rutas únicas
for tiempo_total, ruta in rutas:
    ruta_str = "->".join(ruta)
    if ruta_str not in usadas:
        rutas_unicas.append((tiempo_total, ruta))
        usadas.add(ruta_str)
    if len(rutas_unicas) == 3:
        break

# Mostrar resultados
for idx, (tiempo_total, ruta) in enumerate(rutas_unicas):
    viaje, espera = desglose_tiempos(ruta)
    print(f"\nRuta #{idx+1}: {' -> '.join(ruta)}")
    print(f"  - Tiempo total: {tiempo_total:.2f} h")
    print(f"  - Tiempo de viaje: {viaje:.2f} h")
    print(f"  - Tiempo de espera: {espera:.2f} h")

# Visualizar grafo
G = nx.DiGraph()
for origen, destinos in grafo.items():
    for destino, peso in destinos.items():
        G.add_edge(origen, destino, weight=peso)

pos = nx.spring_layout(G, seed=42)
labels = {nodo: f"{nodo}\n({tiempos_espera[nodo]}h)" for nodo in G.nodes}
plt.figure(figsize=(12, 8))
nx.draw(
    G,
    pos,
    with_labels=True,
    labels=labels,
    node_size=2000,
    node_color="lightgreen",
    font_size=10,
)
nx.draw_networkx_edge_labels(
    G, pos, edge_labels={(u, v): f"{d['weight']}h" for u, v, d in G.edges(data=True)}
)
plt.title("Red de distribución de UniCafé entre universidades")
plt.show()
