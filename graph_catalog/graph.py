from __future__ import annotations

from constants import Weights
from utils import binary_search


class Vertex:
    """Represent vertex of a graph."""

    def __init__(
        self, index: int, outgoing_edges: list[Edge] = [], weights: Weights = {}
    ) -> None:
        self.index = index
        self._outgoing_edges = []
        self._nbrs = []
        for edge in outgoing_edges:
            self.add_edge(edge)
        self.weights = weights

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
    """Represent edge of a graph."""

    def __init__(
        self,
        index: int,
        from_vertices: list[Vertex] = [],
        to_vertices: list[Vertex] = [],
        weights: Weights = {},
    ) -> None:
        self.index = index
        self.from_vertices = from_vertices
        self.to_vertices = to_vertices
        self.weights = weights


class Graph:
    """Represent graph in dynamic manner."""

    def __init__(self, vertices: list[Vertex] = [], edges: list[Edge] = []) -> None:
        self.vertices = vertices
        self.edges = edges
        """List of edges represented as Edge class.
        """
