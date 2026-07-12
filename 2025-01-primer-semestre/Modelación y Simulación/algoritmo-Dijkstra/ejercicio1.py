import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Tiempos de espera en cada ciudad (en horas)
tiempos_espera = {
    "A": 0.0,
    "B": 1.0,
    "C": 1.5,
    "D": 1.2,
    "E": 0.8,
    "F": 1.5,
    "G": 0.7,
    "H": 1.0,
    "I": 1.3,
    "J": 1.0,
    "K": 1.1,
    "L": 1.7,
}

# Nombres de las ciudades
nombres_ciudades = {
    "A": "Ciudad de Guatemala",
    "B": "San Salvador",
    "C": "Tegucigalpa",
    "D": "Managua",
    "E": "San José",
    "F": "Panamá",
    "G": "Santa Ana",
    "H": "Choluteca",
    "I": "León",
    "J": "Liberia",
    "K": "David",
    "L": "Colón",
}

# Aristas con tiempo de viaje entre ciudades
tiempos_viaje = [
    ("A", "B", 5),
    ("A", "G", 4),
    ("A", "H", 9),
    ("A", "I", 12),
    ("B", "C", 6),
    ("B", "I", 10),
    ("G", "C", 5),
    ("G", "D", 7),
    ("C", "D", 8),
    ("C", "H", 3),
    ("C", "I", 6),
    ("D", "E", 8),
    ("D", "I", 2),
    ("I", "E", 7),
    ("I", "J", 6),
    ("E", "F", 9),
    ("E", "J", 3),
    ("J", "K", 4),
    ("J", "L", 7),
    ("K", "F", 5),
    ("K", "L", 6),
    ("F", "L", 3),
]

# Crear grafo dirigido con pesos basados en tiempo total (viaje + espera del destino)
G = nx.DiGraph()
for origen, destino, tiempo in tiempos_viaje:
    peso_total = tiempo + tiempos_espera[destino]
    G.add_edge(
        origen, destino, viaje=tiempo, espera=tiempos_espera[destino], peso=peso_total
    )


# Algoritmo de Dijkstra modificado para retornar ruta más rápida y otras rutas
def dijkstra_k_rutas(G, inicio, fin, k=3):
    rutas = []
    cola = [(0, 0, inicio, [])]  # (tiempo total, solo viaje, nodo actual, camino)
    visitadas = set()

    while cola and len(rutas) < k * 5:
        tiempo_total, viaje_total, actual, camino = heapq.heappop(cola)
        camino = camino + [actual]

        if actual == fin:
            ruta_id = tuple(camino)
            if ruta_id not in visitadas:
                rutas.append((camino, tiempo_total, viaje_total))
                visitadas.add(ruta_id)
            if len(rutas) >= k:
                break

        for vecino in G.successors(actual):
            if vecino not in camino:
                datos = G[actual][vecino]
                nuevo_viaje = viaje_total + datos["viaje"]
                nuevo_total = tiempo_total + datos["peso"]
                heapq.heappush(cola, (nuevo_total, nuevo_viaje, vecino, camino))

    return rutas[:k]


# Ejecutar Dijkstra para obtener rutas desde A hasta L
rutas_encontradas = dijkstra_k_rutas(G, "A", "L", k=3)

# Mostrar resultados
for idx, (ruta, tiempo_total, tiempo_viaje) in enumerate(rutas_encontradas):
    tipo = "Ruta más rápida" if idx == 0 else f"Ruta alternativa {idx}"
    espera_total = tiempo_total - tiempo_viaje
    print(f"{tipo}: {' -> '.join(nombres_ciudades[n] for n in ruta)}")
    print(f"  - Tiempo total: {tiempo_total:.2f} h")
    print(f"    - Tiempo de viaje: {tiempo_viaje:.2f} h")
    print(f"    - Tiempo en colas de espera: {espera_total:.2f} h\n")

# Visualización del grafo
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(18, 12))
nx.draw_networkx_nodes(G, pos, node_color="lightgreen", node_size=1200)
nx.draw_networkx_labels(G, pos, labels=nombres_ciudades, font_size=10)
nx.draw_networkx_edges(G, pos, edge_color="gray")

# Etiquetas con tiempos de viaje + espera
etiquetas = {(u, v): f"{G[u][v]['viaje']}h+{G[u][v]['espera']}h" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas, font_size=8)

# Colores para rutas
colores = ["red", "blue", "green"]
anchos = [3, 2.5, 2]

for idx, (ruta, _, _) in enumerate(rutas_encontradas):
    edges = list(zip(ruta[:-1], ruta[1:]))
    nx.draw_networkx_edges(
        G, pos, edgelist=edges, edge_color=colores[idx], width=anchos[idx]
    )

plt.title("Rutas logísticas desde Ciudad de Guatemala a Colón, Panamá", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()
