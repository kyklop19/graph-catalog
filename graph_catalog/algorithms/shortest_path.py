from math import inf

from graph_catalog.algorithms.searching import bfs_component
from graph_catalog.constants import AdjList, Weights
from graph_catalog.heap import Heap


def backtrack(parents: list[int], end_vertex: int) -> list[int]:
    """Returns sequence of vertices indexes from starting vertex to end vertex based on parent list

    Args:
        parents (list[int]): List where every element represents parent of it's index
        end_vertex (int): Vertex index from where to start backtracking

    Returns:
        list[int]: List of vertices indexes from starting vertex to end vertex
    """
    curr_vertex = end_vertex
    res = []
    while curr_vertex is not None:
        res.append(curr_vertex)
        curr_vertex = parents[curr_vertex]
    return [v for v in reversed(res)]


def find_shortest_path(
    graph: AdjList, start_vertex: int, end_vertex: int
) -> list[int] | None:
    """Finds the shortest path from ``start_vertex`` to ``end_vertex`` in unweighted graph

    Args:
        graph (AdjList): Graph as adjacency list
        start_vertex (int): Vertex from where to start searching
        end_vertex (int): Vertex where to stop searching

    Returns:
        list[int] | None: Path as list of vertex index from start to end if path exists else None
    """
    res = None
    for curr_vertex, dfs_states in bfs_component(graph, start_vertex):
        if curr_vertex == end_vertex:
            res = backtrack(dfs_states.parents, curr_vertex)
            break
    return res


def find_shortest_path_weighted(
    graph: AdjList, start_vertex: int, end_vertex: int, weight_name: str = "length"
) -> list[int] | None:
    """Find shortest path from ``start_vertex`` to ``end_vertex`` in non-negatively weighted graph

    Function is an implementation of Dijkstra's algorithm.

    Args:
        graph (AdjList): Graph as adjacency list
        start_vertex (int): Vertex from where to start searching
        end_vertex (int): Vertex where to end search
        weight_name (str, optional): Name of non-negative weight in the ``graph``. Defaults to "length".

    Returns:
        list[int] | None: Path as list of vertex index from start to end if path exists else None
    """

    res = []
    num_of_V = len(graph)
    distances = [inf] * num_of_V
    parents = [None] * num_of_V

    distances[start_vertex] = 0

    priority_queue = Heap([(inf, vertex) for vertex in range(num_of_V)])
    priority_queue.change_value(0, start_vertex)
    while len(priority_queue) > 0:
        __, curr_vertex = priority_queue.pop()

        if distances[curr_vertex] == inf:
            break
        elif curr_vertex == end_vertex:
            res = backtrack(parents, end_vertex)
            break

        for nbr, weights in graph[curr_vertex]:
            alt = distances[curr_vertex] + weights[weight_name]
            if distances[nbr] > alt:
                distances[nbr] = alt
                priority_queue.change_value(alt, nbr)
                parents[nbr] = curr_vertex

    return res if len(res) != 0 else None
