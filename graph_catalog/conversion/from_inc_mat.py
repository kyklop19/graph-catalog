from constants import AdjList, AdjMat, EdgeList, EdgeTuple, IncMat, NbrTuple
from graph import Edge, Graph, Vertex


def iterate_over_edges(graph: IncMat):
    num_of_V = len(graph)
    num_of_E = len(graph[0])

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

        yield from_v, to_v, directed


def IncMat2AdjMat(graph: IncMat) -> AdjMat:
    num_of_V = len(graph)
    num_of_E = len(graph[0])

    res = []
    for __ in range(num_of_V):
        res.append([0] * num_of_V)

    for from_v, to_v, directed in iterate_over_edges(graph):

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

    for edge, from_v, to_v, directed in enumerate(iterate_over_edges(graph)):

        res[from_v].append(NbrTuple(to_v, {"index": edge}))
        if not directed:
            res[to_v].append(NbrTuple(from_v, {"index": edge}))

    return res


def IncMat2EdgeList(graph: IncMat) -> EdgeList:
    num_of_V = len(graph)
    num_of_E = len(graph[0])

    res = []

    for from_v, to_v, directed in iterate_over_edges(graph):
        res.append(EdgeTuple(from_v, to_v, {"directed": directed}))

    return res


def IncMat2Graph(graph: IncMat) -> Graph:
    num_of_V = len(graph)

    num_of_E = len(graph[0])

    res = Graph()
    for __ in range(num_of_V):
        res.add_vertex()

    for edge in range(num_of_E):
        loop_vertex = -1
        from_vertices = []
        to_vertices = []
        for vertex in range(num_of_V):
            match graph[vertex][edge]:
                case 1:
                    from_vertices.append(vertex)
                case -1:
                    to_vertices.append(vertex)
                case 2:
                    loop_vertex = vertex
                    break
        if loop_vertex != -1:
            res.add_loop(loop_vertex)
        elif len(to_vertices) == 0:
            if len(from_vertices) == 2:
                res.add_undirected_edge(*from_vertices)
            else:
                res.add_undirected_hyperedge(from_vertices)
        else:
            if len(from_vertices) == 1 and len(to_vertices) == 1:
                res.add_directed_edge(from_vertices[0], to_vertices[0])
            else:
                res.add_directed_hyperedge(from_vertices, to_vertices)
    return res
