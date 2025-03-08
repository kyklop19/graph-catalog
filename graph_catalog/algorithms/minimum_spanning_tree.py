from collections import deque
from copy import deepcopy
from math import inf

from constants import EdgeList, EdgeTuple


def find_minimum_spanning_tree(
    graph: EdgeList, weight_name: str = "length"
) -> EdgeList:
    graph = deepcopy(graph)
    res = []
    num_of_components = max(max(v1, v2) for v1, v2, __ in graph)
    vertex_component = [i for i in range(num_of_components)]
    best_edge_for_components = {
        i: EdgeTuple(-1, -1, {weight_name: inf}) for i in range(num_of_components)
    }

    to_visit = deque(graph)
    to_visit_next = deque()

    while num_of_components > 1:
        while len(to_visit) > 0:
            curr_edge = to_visit.pop()
            if vertex_component[curr_edge[0]] != vertex_component[curr_edge[1]]:
                to_visit_next.append(curr_edge)
                if (
                    curr_edge.weights[weight_name]
                    < best_edge_for_components[curr_edge[0]].weights[weight_name]
                ):
                    best_edge_for_components[curr_edge[0]] = curr_edge
                if (
                    curr_edge.weights[weight_name]
                    < best_edge_for_components[curr_edge[1]].weights[weight_name]
                ):
                    best_edge_for_components[curr_edge[1]] = curr_edge
        for component, edge in best_edge_for_components.items():
            res.append(edge)
            del best_edge_for_components[vertex_component[edge[0]]]
            vertex_component[edge[0]] = vertex_component[edge[1]]
            num_of_components -= 1

    return res
