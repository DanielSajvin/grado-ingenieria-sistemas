import networkx as nx
import matplotlib.pyplot as plt


def construir_grafo(aristas, criterio):
    G = nx.DiGraph()
    for arista in aristas:
        peso = arista[criterio]
        if peso is not None:
            G.add_edge(
                arista["origen"],
                arista["destino"],
                weight=peso,
                label=f"{peso} ({criterio})",
            )
    return G


def dijkstra_ruta(grafo, inicio, destino):
    return nx.dijkstra_path(grafo, inicio, destino, weight="weight")


def visualizar_grafo(grafo, ruta=None):
    pos = nx.spring_layout(grafo)
    labels = nx.get_edge_attributes(grafo, "label")
    weights = nx.get_edge_attributes(grafo, "weight")

    nx.draw(
        grafo,
        pos,
        with_labels=True,
        node_color="lightblue",
        edge_color="gray",
        node_size=1500,
        font_size=10,
    )
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)

    if ruta:
        edges_in_path = list(zip(ruta, ruta[1:]))
        nx.draw_networkx_edges(
            grafo, pos, edgelist=edges_in_path, edge_color="red", width=2
        )

    plt.title("Ruta más corta")
    plt.show()
