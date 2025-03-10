from constants import (
    AdjList,
    AdjMat,
    ConversionError,
    EdgeList,
    EdgeTuple,
    IncMat,
    NbrTuple,
)
from graph import (
    DirectedEdge,
    DirectedHyperedge,
    Graph,
    LoopEdge,
    UndirectedEdge,
    UndirectedHyperedge,
)


def Graph2AdjMat(graph: Graph) -> AdjMat:
    """Convert graph from instance of Graph to adjacency matrix

    Args:
        graph (Graph): Graph as instance of Graph without hyperedges

    Raises:
        ConversionError: If graph contains hyperedges

    Returns:
        AdjMat: Graph as adjacency matrix
    """
    res = []
    num_of_V = len(graph.vertices)
    for __ in range(num_of_V):
        res.append([0] * num_of_V)

    for edge in graph.edges:
        if isinstance(edge, UndirectedEdge):
            res[edge.vertices[0].index][edge.vertices[1].index] = 1
            res[edge.vertices[1].index][[edge.vertices[0].index]] = 1
        elif isinstance(edge, DirectedEdge):
            res[edge.source_vertex.index][edge.target_vertex.index] = 1
        elif isinstance(edge, LoopEdge):
            res[edge.vertex.index][edge.vertex.index] = 1
        elif isinstance(edge, UndirectedHyperedge) or isinstance(
            edge, DirectedHyperedge
        ):
            raise ConversionError("AdjMat doesn't support hyperedges")

    return res


def Graph2AdjList(graph: Graph) -> AdjList:
    """Convert graph from instance of Graph to adjacency list

    Args:
        graph (Graph): Graph as instance of Graph without hyperedges

    Raises:
        ConversionError: If graph contains hyperedges

    Returns:
        AdjList: Graph as adjacency list
    """
    res = []
    num_of_V = len(graph.vertices)
    for __ in range(num_of_V):
        res.append([])

    for edge_index, edge in enumerate(graph.edges):
        if isinstance(edge, UndirectedEdge):
            res[edge.vertices[0].index].append(
                NbrTuple(edge.vertices[1].index), {"index": edge_index}
            )
            res[edge.vertices[1].index].append(
                NbrTuple(edge.vertices[0].index), {"index": edge_index}
            )
        elif isinstance(edge, DirectedEdge):
            res[edge.source_vertex.index].append(
                NbrTuple(edge.target_vertex.index), {"index": edge_index}
            )
        elif isinstance(edge, LoopEdge):
            res[edge.vertex.index].append(
                NbrTuple(edge.vertex.index), {"index": edge_index}
            )
        elif isinstance(edge, UndirectedHyperedge) or isinstance(
            edge, DirectedHyperedge
        ):
            raise ConversionError("AdjList doesn't support hyperedges")

    return res


def Graph2EdgeList(graph: Graph) -> EdgeList:
    """Convert graph from instance of `Graph` to `EdgeList`

    Args:
        graph (Graph): Graph as instance of `Graph` without hyperedges

    Raises:
        ConversionError: If graph contains hyperedges

    Returns:
        EdgeList: Graph as `EdgeList`
    """
    res = []
    for edge in graph.edges:
        if isinstance(edge, UndirectedEdge):
            res.append(
                EdgeTuple(
                    edge.vertices[0].index, edge.vertices[1].index, {"directed": False}
                )
            )
        elif isinstance(edge, DirectedEdge):
            res.append(
                EdgeTuple(
                    edge.source_vertex.index,
                    edge.target_vertex.index,
                    {"directed": True},
                )
            )
        elif isinstance(edge, LoopEdge):
            res.append(
                EdgeTuple(edge.vertex.index, edge.vertex.index, {"directed": True})
            )
        elif isinstance(edge, UndirectedHyperedge) or isinstance(
            edge, DirectedHyperedge
        ):
            raise ConversionError("EdgeList doesn't support hyperedges")

    return res


def Graph2IncMat(graph: Graph) -> IncMat:
    """Convert graph from instance of `Graph` to `IncMat`

    Graph can contain hyperedges.

    Args:
        graph (Graph): Graph as instance of `Graph`

    Returns:
        IncMat: Graph as `IncMat`
    """
    res = []
    num_of_V = len(graph.vertices)
    for __ in range(num_of_V):
        res.append([])

    for edge in graph.edges:
        for i in range(num_of_V):
            res[i].append(0)

        if isinstance(edge, UndirectedEdge):
            for vertex in edge.vertices:
                res[vertex.index][-1] = 1
        elif isinstance(edge, DirectedEdge):
            res[edge.source_vertex.index][-1] = 1
            res[edge.target_vertex.index][-1] = -1
        elif isinstance(edge, LoopEdge):
            res[edge.vertex.index][-1] = 2
        elif isinstance(edge, UndirectedHyperedge):
            for vertex in edge.vertices:
                res[vertex.index][-1] = 1
        elif isinstance(edge, DirectedHyperedge):
            for vertex in edge.source_vertices:
                res[vertex.index][-1] = 1
            for vertex in edge.target_vertices:
                res[vertex.index][-1] = -1

    return res
