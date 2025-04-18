from copy import deepcopy

from graph_catalog.constants import AdjList, AdjMat, EdgeList, EdgeTuple, IncMat
from graph_catalog.graph import Edge, Graph, Vertex


def AdjList2EdgeList(graph: AdjList) -> EdgeList:
    """Convert graph from adjacency list to edge list

    Args:
        graph (AdjList): Graph as adjacency list

    Returns:
        EdgeList: Graph as edge list
    """

    num_of_V = len(graph)

    res = []

    added_edges = set()

    for source_vertex, source_nbrs in enumerate(graph):
        for source_nbr in source_nbrs:

            index = source_nbr.weights["index"]

            if index in added_edges:
                continue
            else:
                added_edges.add(index)

            weights = deepcopy(source_nbr.weights)
            del weights["index"]

            directed = True
            if source_vertex != source_nbr[0]:
                for nbr in graph[source_nbr.vertex]:
                    if nbr.weights["index"] == index:
                        directed = False
                        break

            weights["directed"] = directed

            res.append(EdgeTuple(source_vertex, source_nbr[0], weights))

    return res


def AdjList2AdjMat(graph: AdjList) -> AdjMat:
    """Convert graph from adjacency list to adjacency matrix

    Args:
        graph (AdjList): Graph as adjacency list

    Returns:
        AdjMat: Graph as adjacency matrix
    """
    res = []
    size = len(graph)

    for starting_vertex, edges in enumerate(graph):

        adj_list = [0] * size

        for vertex in edges:
            adj_list[vertex[0]] = 1

        res.append(adj_list)
    return res


def AdjList2IncMat(graph: AdjList) -> IncMat:
    """Converts graph from adjacency list to incidence matrix

    Args:
        graph (AdjList): Graph as adjacency list

    Returns:
        IncMat: Graph as incidence matrix
    """
    num_of_V = len(graph)

    res = []
    for __ in range(num_of_V):
        res.append([])

    num_of_E = 0

    for starting_vertex, nbrs in enumerate(graph):

        for nbr in nbrs:

            i = nbr.weights["index"]

            missing_E = max((i + 1) - num_of_E, 0)

            for __ in range(missing_E):
                for row in res:
                    row.append(0)
            num_of_E += missing_E

            if starting_vertex == nbr[0]:
                res[starting_vertex][i] = 2
            else:
                res[starting_vertex][i] = 1
                if res[nbr[0]][i] == 0:
                    res[nbr[0]][i] = -1

    return res


def AdjList2Graph(graph: AdjList) -> Graph:
    """Converts graph from adjacency list to instance of Graph

    Args:
        graph (AdjList): Graph as adjacency list

    Returns:
        Graph: Graph as instance of Graph
    """

    num_of_V = len(graph)

    res = Graph()

    for __ in range(num_of_V):
        res.add_vertex()

    added_edges = set()

    for source_vertex, source_nbrs in enumerate(graph):
        for source_nbr in source_nbrs:

            index = source_nbr.weights["index"]

            if index in added_edges:
                continue
            else:
                added_edges.add(index)

            weights = deepcopy(source_nbr.weights)
            del weights["index"]

            directed = True
            if source_vertex != source_nbr[0]:
                for nbr in graph[source_nbr.vertex]:
                    if nbr.weights["index"] == index:
                        directed = False
                        break

            if directed:
                if source_vertex == source_nbr[0]:
                    res.add_loop(source_vertex, weights)
                else:
                    res.add_directed_edge(source_vertex, source_nbr[0], weights)
            else:
                res.add_undirected_edge(source_vertex, source_nbr[0], weights)

    return res
