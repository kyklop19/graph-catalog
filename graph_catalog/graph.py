from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterator

from constants import Weights
from utils import binary_search


class Vertex:
    """Represent vertex of a graph."""

    def __init__(
        self, index: int, outgoing_edges: list[Edge] = [], weights: Weights = {}
    ) -> None:
        self.index = index
        self._outgoing_edges = []
        self._nbrs = set()
        for edge in outgoing_edges:
            self.add_edge(edge)
        self.weights = weights

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return all(
                (
                    self.index == other.index,
                    self.outgoing_edges == other.outgoing_edges,
                    self.nbrs == other.nbrs,
                    self.weights == other.weights,
                )
            )
        else:
            return NotImplemented

    @property
    def outgoing_edges(self) -> list[Edge]:
        return self._outgoing_edges

    @property
    def nbrs(self) -> set[Vertex]:
        return self._nbrs

    def add_edge(self, edge: Edge) -> None:
        """Add edge as an outgoing edge and update list of neighbors

        Args:
            edge (Edge): Edge in which this vertex is source vertex
        """
        self._outgoing_edges.append(edge)

        for nbr in edge.get_target_vertices(self):
            self._nbrs.add(nbr)


class Edge(ABC):
    """Represent edge of a graph."""

    def __init__(self, index: int, weights: Weights = {}) -> None:
        self.index = index
        self.weights = weights

    def __eq__(self, other):
        if isinstance(other, Edge):
            return all(self.index == other.index, self.weights == other.weights)
        else:
            return NotImplemented

    @abstractmethod
    def get_target_vertices(self, source_vertex: Vertex | None) -> Iterator[Vertex]:
        pass


class UndirectedEdge(Edge):

    def __init__(
        self, index: int, vertex1: Vertex, vertex2: Vertex, weights: Weights = {}
    ) -> None:
        super().__init__(index, weights)

        self.vertices = (vertex1, vertex2)

    def __eq__(self, other):
        if isinstance(other, UndirectedEdge):
            return super().__eq__(other) and self.vertices == other.vertices
        else:
            return NotImplemented

    def get_target_vertices(self, source_vertex: Vertex | None) -> Iterator[Vertex]:
        for vertex in self.vertices:
            if vertex != source_vertex:
                yield vertex


class DirectedEdge(Edge):

    def __init__(
        self,
        index: int,
        source_vertex: Vertex,
        target_vertex: Vertex,
        weights: Weights = {},
    ) -> None:
        super().__init__(index, weights)

        self.source_vertex = source_vertex
        self.target_vertex = target_vertex

    def __eq__(self, other):
        if isinstance(other, DirectedEdge):
            return super().__eq__(other) and all(
                self.source_vertex == other.source_vertex,
                self.target_vertex == other.target_vertex,
            )
        else:
            return NotImplemented

    def get_target_vertices(self, __: Vertex | None = None) -> Iterator[Vertex]:
        yield self.target_vertex


class LoopEdge(Edge):

    def __init__(self, index: int, vertex: Vertex, weights: Weights = {}) -> None:
        super().__init__(index, weights)

        self.vertex = vertex

    def __eq__(self, other):
        if isinstance(other, LoopEdge):
            return super().__eq__(other) and self.vertex == other.vertex
        else:
            return NotImplemented

    def get_target_vertices(self, __: Vertex | None = None) -> Iterator[Vertex]:
        yield self.vertex


class UndirectedHyperedge(Edge):

    def __init__(
        self, index: int, vertices: list[Vertex], weights: Weights = {}
    ) -> None:
        super().__init__(index, weights)

        self.vertices = vertices

    def __eq__(self, other):
        if isinstance(other, UndirectedHyperedge):
            return super().__eq__(other) and self.vertices == other.vertices
        else:
            return NotImplemented

    def get_target_vertices(self, source_vertex: Vertex | None) -> Iterator[Vertex]:
        for vertex in self.vertices:
            if vertex != source_vertex:
                yield vertex


class DirectedHyperedge(Edge):

    def __init__(
        self,
        index: int,
        source_vertices: list[Vertex],
        target_vertices: list[Vertex],
        weights: Weights = {},
    ) -> None:
        super().__init__(index, weights)

        self.source_vertices = source_vertices
        self.target_vertices = target_vertices

    def __eq__(self, other):
        if isinstance(other, DirectedHyperedge):
            return super().__eq__(other) and all(
                self.source_vertices == other.source_vertices,
                self.target_vertices == other.target_vertices,
            )
        else:
            return NotImplemented

    def get_target_vertices(self, __: Vertex | None = None) -> Iterator[Vertex]:
        for vertex in self.target_vertices:
            yield vertex


class Graph:
    """Represent graph in dynamic manner."""

    def __init__(self, vertices: list[Vertex] = [], edges: list[Edge] = []) -> None:
        self._vertices = vertices
        self._edges = edges
        """List of edges represented as Edge class.
        """

    def __eq__(self, other):
        if isinstance(other, Graph):
            return self.vertices == other.vertices and self.edges == other.edges
        else:
            return NotImplemented

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges

    def add_vertex(self, weights: Weights = {}) -> None:
        new_vertex_index = len(self._vertices)
        new_vertex = Vertex(new_vertex_index, weights=weights)
        self._vertices.append(new_vertex)

    def add_undirected_edge(
        self, vertex1_index: int, vertex2_index: int, weights: Weights = {}
    ) -> None:
        vertex1 = self._vertices[vertex1_index]
        vertex2 = self._vertices[vertex2_index]

        new_edge_index = len(self._edges)
        new_edge = UndirectedEdge(new_edge_index, vertex1, vertex2, weights)
        self._edges.append(new_edge)

        vertex1.add_edge(new_edge)
        vertex2.add_edge(new_edge)

    def add_directed_edge(
        self, source_vertex_index: int, target_vertex_index: int, weights: Weights = {}
    ) -> None:
        source_vertex = self._vertices[source_vertex_index]
        target_vertex = self._vertices[target_vertex_index]

        new_edge_index = len(self._edges)
        new_edge = DirectedEdge(new_edge_index, source_vertex, target_vertex, weights)
        self._edges.append(new_edge)

        source_vertex.add_edge(new_edge)

    def add_loop(self, vertex_index: int, weights: Weights = {}) -> None:
        vertex = self._vertices[vertex_index]

        new_edge_index = len(self._edges)
        new_edge = LoopEdge(new_edge_index, vertex, weights)
        self._edges.append(new_edge)

        vertex.add_edge(new_edge)

    def add_undirected_hyperedge(
        self, vertices_indexes: list[int], weights: Weights = {}
    ) -> None:
        vertices = [self._vertices[index] for index in vertices_indexes]

        new_edge_index = len(self._edges)
        new_edge = UndirectedHyperedge(new_edge_index, vertices, weights)
        self._edges.append(new_edge)

        for vertex in vertices:
            vertex.add_edge(new_edge)

    def add_directed_hyperedge(
        self,
        source_vertices_indexes: list[int],
        target_vertices_indexes: list[int],
        weights: Weights = {},
    ) -> None:

        source_vertices = [self._vertices[index] for index in source_vertices_indexes]
        target_vertices = [self._vertices[index] for index in target_vertices_indexes]

        new_edge_index = len(self._edges)
        new_edge = UndirectedHyperedge(
            new_edge_index, source_vertices, target_vertices, weights
        )
        self._edges.append(new_edge)

        for vertex in source_vertices:
            vertex.add_edge(new_edge)
