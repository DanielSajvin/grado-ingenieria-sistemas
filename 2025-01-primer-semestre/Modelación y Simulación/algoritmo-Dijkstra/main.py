import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Datos de las ciudades y rutas
rutas = {
    ("A", "C"): (95, 60),
    ("A", "D"): (215, 50),
    ("C", "B"): (140, 65),
    ("B", "F"): (515, 45),
    ("D", "E"): (1000, 70),
    ("E", "F"): (290, 80),
    ("C", "G"): (475, 55),
    ("F", "G"): (170, 75),
    ("E", "H"): (1200, 65),
    ("H", "I"): (660, 70),
    ("I", "J"): (1350, 80),
    ("J", "K"): (385, 90),
    ("K", "L"): (2500, 75),
    ("L", "M"): (600, 70),
}

nombres_ciudades = {
    "A": "Nueva York",
    "B": "Washington D.C.",
    "C": "Filadelfia",
    "D": "Boston",
    "E": "Chicago",
    "F": "Detroit",
    "G": "Cleveland",
    "H": "Atlanta",
    "I": "Miami",
    "J": "Dallas",
    "K": "Houston",
    "L": "San Francisco",
    "M": "Los Ángeles",
}

# Construcción del grafo ponderado por tiempo
G = nx.DiGraph()
for (origen, destino), (distancia, velocidad) in rutas.items():
    tiempo = distancia / velocidad
    G.add_edge(origen, destino, distancia=distancia, velocidad=velocidad, tiempo=tiempo)
    G.add_edge(destino, origen, distancia=distancia, velocidad=velocidad, tiempo=tiempo)


def dijkstra_k_rutas(G, inicio, fin, k=3):
    rutas = []
    cola = [(0, inicio, [])]
    visitados_rutas = set()

    while cola and len(rutas) < k * 5:  # Explorar más para obtener alternativas
        tiempo_total, nodo, camino = heapq.heappop(cola)
        camino = camino + [nodo]
        if nodo == fin:
            ruta_id = tuple(camino)
            if ruta_id not in visitados_rutas:
                rutas.append((camino, tiempo_total))
                visitados_rutas.add(ruta_id)
            if len(rutas) >= k:
                break
        for vecino in G.neighbors(nodo):
            if vecino not in camino:  # evitar ciclos
                tiempo_viaje = G[nodo][vecino]["tiempo"]
                heapq.heappush(cola, (tiempo_total + tiempo_viaje, vecino, camino))
    return rutas[:k]


# Obtener tres rutas desde A hasta M
rutas_resultado = dijkstra_k_rutas(G, "A", "M", k=3)

# Mostrar rutas
for idx, (ruta, tiempo) in enumerate(rutas_resultado):
    tipo = "Ruta más rápida" if idx == 0 else f"Ruta alternativa {idx}"
    print(f"{tipo}: {' -> '.join(nombres_ciudades[n] for n in ruta)}")
    print(f"Tiempo total estimado: {tiempo:.2f} horas\n")

# Visualización del grafo
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(18, 12))
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=1000)
nx.draw_networkx_labels(G, pos, labels=nombres_ciudades, font_size=10)
nx.draw_networkx_edges(G, pos, edge_color="gray")

# Etiquetas de tiempo
labels = {
    (u, v): f"{G[u][v]['distancia']} km\n{G[u][v]['tiempo']:.1f} h"
    for u, v in G.edges()
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

# Colores para rutas
colores = ["red", "green", "blue"]
anchos = [3, 2.5, 2]

for idx, (ruta, _) in enumerate(rutas_resultado):
    edges = list(zip(ruta[:-1], ruta[1:]))
    nx.draw_networkx_edges(
        G, pos, edgelist=edges, edge_color=colores[idx], width=anchos[idx]
    )

plt.title("Comparación de rutas desde Nueva York a Los Ángeles", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()
