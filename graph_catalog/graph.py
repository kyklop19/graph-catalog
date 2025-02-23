from constants import Weight
from utils import binary_search


class Vertex:

    def __init__(
        self, index: int, outgoing_edges: list[Edge] = [], weight: Weight = {}
    ) -> None:
        self.index = index
        self._outgoing_edges = []
        self._nbrs = []
        for edge in outgoing_edges:
            self.add_edge(edge)
        self.weight = weight

    @property
    def outgoing_edges(self) -> list[Edge]:
        return self._outgoing_edges

    @property
    def nbrs(self) -> list[Vertex]:
        return self._nbrs

    def add_edge(self, edge: Edge) -> None:
        """Add edge as an outgoing edge and update list of neighbors

        Args:
            edge (Edge): _description_
        """
        self._outgoing_edges.append(edge)
        new_nbrs = edge.to_vertices
        for nbr in new_nbrs:
            isFound, index = binary_search(self._nbrs, nbr, key=lambda x: x.index)
            if not isFound:
                self._nbrs.insert(index, nbr)


class Edge:

    def __init__(
        self,
        index: int,
        from_vertices: list[Vertex] = [],
        to_vertices: list[Vertex] = [],
        weight: Weight = {},
    ):
        self.index = index
        self.from_vertices = from_vertices
        self.to_vertices = to_vertices
        self.weight = weight


class Graph:

    def __init__(self, vertices: list[Vertex] = [], edges: list[Edge] = []):
        self.vertices = vertices
        self.edges = edges
