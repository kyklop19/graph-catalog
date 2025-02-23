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
    for edge in enumerate(graph):
        res.append(edge)
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
            adj_list[vertex] = 1

        res.append(adj_list)
    return res


def AdjList2IncMat(graph: AdjList) -> IncMat:
    pass


def AdjList2Graph(graph: AdjList) -> Graph:
    pass
