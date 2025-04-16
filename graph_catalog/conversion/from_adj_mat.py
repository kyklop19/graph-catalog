from graph_catalog.constants import (
    AdjList,
    AdjMat,
    EdgeList,
    EdgeTuple,
    IncMat,
    NbrTuple,
)
from graph_catalog.graph import Edge, Graph, Vertex


def AdjMat2EdgeList(graph: AdjMat) -> EdgeList:
    """Converts graph from adjacency matrix to edge list

    Args:
        graph (AdjMat): Graph as adjacency matrix

    Returns:
        EdgeList: Graph as edge list
    """

    num_of_V = len(graph)

    res = []

    for from_v in range(num_of_V):
        for to_v in range(num_of_V - from_v):
            to_v += from_v
            if graph[from_v][to_v] == 1:
                directed = from_v == to_v or graph[from_v][to_v] != graph[to_v][from_v]
                res.append(EdgeTuple(from_v, to_v, {"directed": directed}))

    return res


def AdjMat2AdjList(graph: AdjMat) -> AdjList:
    """Converts graph from adjacency matrix to adjacency list

    Args:
        graph (AdjMat): Graph as adjacency matrix

    Returns:
        AdjList: Graph as adjacency list
    """
    num_of_V = len(graph)

    res = []

    for __ in range(num_of_V):
        res.append([])

    index = 0

    for from_v in range(num_of_V):
        for to_v in range(num_of_V - from_v):
            to_v += from_v
            if graph[from_v][to_v] == 1:
                res[from_v].append(NbrTuple(to_v, {"index": index}))
                if from_v != to_v and graph[to_v][from_v] == 1:
                    res[to_v].append(NbrTuple(from_v, {"index": index}))
                index += 1

    return res


def AdjMat2IncMat(graph: AdjMat) -> IncMat:
    """Converts graph from adjacency matrix to incidence matrix

    Args:
        graph (AdjMat): Graph as adjacency matrix

    Returns:
        IncMat: Graph as incidence matrix
    """

    size = len(graph)

    res = []
    for __ in range(size):
        res.append([])

    for from_v in range(size):
        for to_v in range(size - from_v):
            to_v += from_v
            if graph[from_v][to_v] == 0:
                continue

            for vertex in res:
                vertex.append(0)

            if from_v == to_v:
                res[from_v][to_v] = 2
                continue

            res[from_v][-1] = 1
            if graph[to_v][from_v] == 0:
                res[to_v][-1] = -1
            else:
                res[to_v][-1] = 1
    return res


def AdjMat2Graph(graph: AdjMat) -> Graph:
    """Converts graph from adjacency matrix to instance of Graph

    Args:
        graph (AdjMat): Graph as adjacency matrix

    Returns:
        Graph: Graph as instance of Graph
    """
    num_of_V = len(graph)

    res = Graph()
    for __ in range(num_of_V):
        res.add_vertex()

    for from_v in range(num_of_V):
        for to_v in range(num_of_V - from_v):
            to_v += from_v
            if graph[from_v][to_v] == 0:
                continue

            if from_v == to_v:
                res.add_loop(from_v)
                continue

            if graph[to_v][from_v] == 0:
                res.add_directed_edge(from_v, to_v)
            else:
                res.add_undirected_edge(from_v, to_v)
    return res
