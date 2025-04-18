from copy import deepcopy

from graph_catalog.constants import AdjList, AdjMat, EdgeList, IncMat, NbrTuple
from graph_catalog.graph import Edge, Graph, Vertex


def EdgeList2AdjMat(graph: EdgeList) -> AdjMat:
    """Converts graph from edge list to adjacency matrix

    Args:
        graph (EdgeList): Graph as edge list

    Returns:
        AdjMat: Graph as adjacency matrix
    """

    num_of_V = max(max(graph, key=lambda x: max(x[0], x[1]))[0:2]) + 1

    res = []

    for __ in range(num_of_V):
        res.append([0] * num_of_V)

    for edge in graph:
        res[edge[0]][edge[1]] = 1
        if not edge.weights["directed"]:
            res[edge[1]][edge[0]] = 1

    return res


def EdgeList2AdjList(graph: EdgeList) -> AdjList:
    """Converts graph from edge list to adjacency list

    Args:
        graph (EdgeList): Graph as edge list

    Returns:
        AdjList: Graph as adjacency list
    """

    res = []

    num_of_V = max(max(graph, key=lambda x: max(x[0], x[1]))[0:2]) + 1

    for __ in range(num_of_V):
        res.append([])

    for edge_index, edge in enumerate(graph):
        res[edge[0]].append(NbrTuple(edge[1], {"index": edge_index}))
        if not edge.weights["directed"]:
            res[edge[1]].append(NbrTuple(edge[0], {"index": edge_index}))

    return res


def EdgeList2IncMat(graph: EdgeList) -> IncMat:
    """Converts graph from edge list to incidence matrix

    Args:
        graph (EdgeList): Graph as edge list

    Returns:
        IncMat: Graph as incidence matrix
    """
    res = []
    num_of_V = max(max(graph, key=lambda x: max(x[0], x[1]))[0:2]) + 1
    num_of_E = len(graph)

    for __ in range(num_of_V):
        res.append([0] * num_of_E)

    for edge_index, edge in enumerate(graph):
        if edge[0] == edge[1]:
            res[edge[0]][edge_index] = 2
        else:
            res[edge[0]][edge_index] = 1
            if edge.weights["directed"]:
                res[edge[1]][edge_index] = -1
            else:
                res[edge[1]][edge_index] = 1
    return res


def EdgeList2Graph(graph: EdgeList) -> Graph:
    """Converts graph from edge list to instance of Graph

    Args:
        graph (EdgeList): Graph as edge list

    Returns:
        Graph: Graph as instance of Graph
    """

    num_of_V = max(max(v1, v2) for v1, v2, __ in graph) + 1

    res = Graph()

    for __ in range(num_of_V):
        res.add_vertex()

    for edge in graph:
        directed = edge.weights["directed"]
        weights = deepcopy(edge.weights)
        del weights["directed"]
        if directed:
            if edge[0] == edge[1]:
                res.add_loop(edge[0])
            else:
                res.add_directed_edge(edge[0], edge[1], weights)
        else:
            res.add_undirected_edge(edge[0], edge[1], weights)

    return res
