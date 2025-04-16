from pyvis.network import Network

from graph_catalog.constants import ROOT_PATH, EdgeList


def visualize_edge_list(graph: EdgeList) -> None:
    num_of_V = max(max(v1, v2) for v1, v2, __ in graph) + 1

    net = Network(directed=True, font_color="black")
    net.toggle_physics(True)
    net.show_buttons(filter_=["physics"])

    for i in range(num_of_V):
        net.add_node(f"{i}")

    for i, (v1, v2, weights) in enumerate(graph):
        net.add_edge(
            str(v1),
            str(v2),
            label=f"{i} | {" | ".join(f'{name}: {value}' for name, value in weights.items())}",
        )

    with open(str(ROOT_PATH / "data" / "graph.html"), "w") as f:
        f.write(net.generate_html("graph.html", notebook=False))
