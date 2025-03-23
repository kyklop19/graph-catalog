from math import inf

from graph_catalog.algorithms.searching import bfs_component
from graph_catalog.constants import AdjList, Weights
from graph_catalog.heap import Heap


def backtrack(parents: list[int], end_vertex: int) -> list[int]:
    curr_vertex = end_vertex
    res = []
    while curr_vertex is not None:
        res.append(curr_vertex)
        curr_vertex = parents[curr_vertex]
    return reversed(res)


def find_shortest_path(graph: AdjList, start_vertex: int, end_vertex: int) -> list[int]:
    res = []
    for curr_vertex, __, parents in bfs_component(graph, start_vertex):
        if curr_vertex == end_vertex:
            res = backtrack(parents, curr_vertex)
            break
    return res


def find_shortest_path_weighted(
    graph: AdjList, start_vertex: int, end_vertex: int, weight_name: str = "length"
) -> list[int]:
    res = []
    num_of_V = len(graph)
    distances = [inf] * num_of_V
    parents = [None] * num_of_V

    distances[start_vertex] = 0

    priority_queue = Heap([(inf, vertex) for vertex in range(num_of_V)])
    priority_queue.change_value(0, start_vertex)
    while len(priority_queue) > 0:
        __, curr_vertex = priority_queue.pop()

        if curr_vertex == end_vertex:
            res = backtrack(parents, end_vertex)
            break

        for nbr in graph[curr_vertex]:
            alt = distances[curr_vertex] + nbr.weights[weight_name]
            if distances[nbr] > alt:
                distances[nbr] = alt
                priority_queue.change_value(alt, nbr)
                parents[nbr] = curr_vertex

    return res
