from constants import AdjList, AdjMat, EdgeList, IncMat, NbrTuple
from graph import Edge, Graph, Vertex


def EdgeList2AdjMat(graph: EdgeList) -> AdjMat:

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

    num_of_V = max(max(graph, key=lambda x: max(x[0], x[1]))[0:2]) + 1

    vertices = [Vertex(i) for i in range(num_of_V)]
    edges = []

    for i, edge in enumerate(graph):
        edges.append(
            Edge(
                i,
            )
        )
