from constants import AdjList, AdjMat, EdgeList, EdgeTuple, IncMat, NbrTuple
from graph import Edge, Graph, Vertex


def IncMat2AdjMat(graph: IncMat) -> AdjMat:
    num_of_V = len(graph)
    num_of_E = len(graph[0])

    res = []
    for __ in range(num_of_V):
        res.append([0] * num_of_V)

    for edge in range(num_of_E):
        directed = True
        from_v = None
        to_v = None
        for vertex in range(num_of_V):
            inc = graph[vertex][edge]
            if inc == 1:
                if from_v is None:
                    from_v = vertex
                elif to_v is None:
                    to_v = vertex
                    directed = False
                else:
                    raise Exception
            elif inc == -1:
                if to_v is None:
                    to_v = vertex
                else:
                    raise Exception
            elif inc == 2:
                if from_v is None and to_v is None:
                    from_v = vertex
                    to_v = vertex
                    break
                else:
                    raise Exception

        res[from_v][to_v] = 1
        if not directed:
            res[to_v][from_v] = 1

    return res


def IncMat2AdjList(graph: IncMat) -> AdjList:
    num_of_V = len(graph)
    num_of_E = len(graph[0])

    res = []
    for __ in range(num_of_V):
        res.append([])

    for edge in range(num_of_E):
        directed = True
        from_v = None
        to_v = None
        for vertex in range(num_of_V):
            inc = graph[vertex][edge]
            if inc == 1:
                if from_v is None:
                    from_v = vertex
                elif to_v is None:
                    to_v = vertex
                    directed = False
                else:
                    raise Exception
            elif inc == -1:
                if to_v is None:
                    to_v = vertex
                else:
                    raise Exception
            elif inc == 2:
                if from_v is None and to_v is None:
                    from_v = vertex
                    to_v = vertex
                    break
                else:
                    raise Exception

        res[from_v].append(NbrTuple(to_v, {"index": edge}))
        if not directed:
            res[to_v].append(NbrTuple(from_v, {"index": edge}))

    return res


def IncMat2EdgeList(graph: IncMat) -> EdgeList:
    num_of_V = len(graph)
    num_of_E = len(graph[0])

    res = []

    for edge in range(num_of_E):
        directed = True
        from_v = None
        to_v = None
        for vertex in range(num_of_V):
            inc = graph[vertex][edge]
            if inc == 1:
                if from_v is None:
                    from_v = vertex
                elif to_v is None:
                    to_v = vertex
                    directed = False
                else:
                    raise Exception
            elif inc == -1:
                if to_v is None:
                    to_v = vertex
                else:
                    raise Exception
            elif inc == 2:
                if from_v is None and to_v is None:
                    from_v = vertex
                    to_v = vertex
                    break
                else:
                    raise Exception

        res.append(EdgeTuple(from_v, to_v, {"directed": directed}))

    return res


def IncMat2Graph(graph: IncMat) -> Graph:
    pass
