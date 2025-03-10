from constants import AdjList, AdjMat, EdgeList, IncMat
from graph import Edge, Graph, Vertex


def AdjList2EdgeList(graph: AdjList) -> EdgeList:
    """Convert graph from adjacency list to edge list

    Args:
        graph (AdjList): Graph as adjacency list

    Returns:
        EdgeList: Graph as edge list
    """

    res = []
    for starting_vertex, nbrs in enumerate(graph):
        for nbr in nbrs:
            pass
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

    num_of_V = len(graph)

    res = Graph()

    for __ in range(num_of_V):
        res.add_vertex()

    for source_vertex, source_nbrs in enumerate(graph):
        for source_nbr in source_nbrs:

            index = source_nbr.weights["index"]
            directed = True
            for nbr in graph[source_nbr.vertex]:
                if nbr.weights["index"] == index:
                    directed = False
                    break

    return res
