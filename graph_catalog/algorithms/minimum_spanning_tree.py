from collections import deque
from copy import deepcopy
from math import inf

from graph_catalog.constants import EdgeList, EdgeTuple


def find_minimum_spanning_tree(
    graph: EdgeList, weight_name: str = "length"
) -> EdgeList:
    """Returns a minimum spanning tree of the connected graph as `EdgeList`

    This function is implemented as Borůvka's algorithm. It takes all
    vertices of the graph as a new graph. Until the new graph is connected for
    each component it adds edge with the lowest weight that connects two
    different components to the new graph.

    Args:
        graph (EdgeList): **Connected** graph as `EdgeList` with **numerically weighted edges**
        weight_name (str, optional): Name of edge weight that has numerical value. Defaults to "length".

    Returns:
        EdgeList: Minimum spanning tree of the graph as `EdgeList`
    """
    graph = deepcopy(graph)
    res = []
    num_of_V = max(max(v1, v2) for v1, v2, __ in graph) + 1
    num_of_components = num_of_V
    vertex_component = [i for i in range(num_of_V)]
    minimum_edges = {i: None for i in range(num_of_components)}

    to_visit = deque(graph)
    to_visit_next = deque()

    while len(to_visit) > 0 or len(to_visit_next) > 0:
        while len(to_visit) > 0:
            curr_edge = to_visit.pop()
            is_better = False
            if vertex_component[curr_edge[0]] != vertex_component[curr_edge[1]]:
                print(curr_edge)
                for vertex_index in range(2):
                    minimum_edge = minimum_edges[
                        vertex_component[curr_edge[vertex_index]]
                    ]
                    if (
                        minimum_edge is None
                        or curr_edge.weights[weight_name]
                        < minimum_edge.weights[weight_name]
                    ):
                        if minimum_edge is not None:
                            to_visit_next.append(minimum_edge)
                        minimum_edges[vertex_component[curr_edge[vertex_index]]] = (
                            curr_edge
                        )
                        is_better = True

                if not is_better:
                    to_visit_next.append(curr_edge)

        print(minimum_edges)

        for component, edge in minimum_edges.items():
            if edge is None:
                continue
            for vertex_index in range(2):
                v_comp = vertex_component[edge[vertex_index]]
                if minimum_edges[v_comp] == edge:
                    minimum_edges[v_comp] = None

            res.append(edge)
            old_component = vertex_component[edge[0]]
            for vertex in range(num_of_V):
                if vertex_component[vertex] == old_component:
                    vertex_component[vertex] = vertex_component[edge[1]]

        if len(to_visit) == 0:
            to_visit = to_visit_next
            to_visit_next = deque()

    return res
