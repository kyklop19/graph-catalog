from constants import AdjList, AdjMat, EdgeList, IncMat
from graph import Edge, Graph, Vertex


def AdjMat2EdgeList(graph: AdjMat) -> EdgeList:
    pass


def AdjMat2AdjList(graph: AdjMat) -> AdjList:
    pass


def AdjMat2IncMat(graph: AdjMat) -> IncMat:

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
    pass
