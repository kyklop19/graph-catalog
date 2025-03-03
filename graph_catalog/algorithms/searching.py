from collections import deque, namedtuple
from enum import IntEnum
from math import inf
from typing import Iterator

from constants import AdjList

DFSStates = namedtuple("DFSStates", ("parents", "opening_orders", "closing_orders"))
BFSStates = namedtuple("BFSStates", ("parents", "distances"))


class SearchState(IntEnum):
    UNVISITED = 0
    OPENED = 1
    CLOSED = 2


def _dfs_component(
    graph: AdjList,
    start_vertex: int,
    orders: tuple[int, int],
    dfs_states: DFSStates[list[int | None], list[int], list[int]],
) -> Iterator[
    tuple[int, tuple[int, int], DFSStates[list[int | None], list[int], list[int]]]
]:

    opening_order = orders[0]
    closing_order = orders[1]

    parents = dfs_states.parents
    opening_orders = dfs_states.opening_orders
    closing_orders = dfs_states.closing_orders

    to_visit = deque()
    to_visit.append(start_vertex)

    while len(to_visit) != 0:
        curr_vertex = to_visit[-1]
        if opening_orders[curr_vertex] == -1:
            opening_orders[curr_vertex] = opening_order
            opening_order += 1
        elif closing_orders[curr_vertex] == -1:
            closing_orders[curr_vertex] = closing_order
            closing_order += 1
            to_visit.pop()
            continue
        else:
            to_visit.pop()
            continue

        yield (
            curr_vertex,
            (opening_order, closing_order),
            DFSStates(parents, opening_orders, closing_orders),
        )

        for nbr, __ in reversed(graph[curr_vertex]):
            if opening_orders[nbr] == -1:
                parents[nbr] = curr_vertex
                to_visit.append(nbr)


def dfs_component(
    graph: AdjList,
    start_vertex: int = 0,
) -> Iterator[tuple[int, DFSStates[list[int | None], list[int], list[int]]]]:
    length = len(graph)
    orders = (0, 0)
    dfs_states = DFSStates(
        [None] * length,
        [-1] * length,
        [-1] * length,
    )

    for curr_vertex, __, curr_dfs_states in _dfs_component(
        graph, start_vertex, orders, dfs_states
    ):
        yield (curr_vertex, curr_dfs_states)


def dfs(
    graph: AdjList, start_vertex: int = 0
) -> Iterator[tuple[int, DFSStates[list[int | None], list[int], list[int]]]]:

    length = len(graph)
    orders = (0, 0)
    dfs_states = DFSStates(
        [None] * length,
        [-1] * length,
        [-1] * length,
    )

    for i in range(length):
        if dfs_states.opening_orders[i] == -1:
            for curr_vertex, curr_orders, curr_dfs_states in _dfs_component(
                graph, i, orders, dfs_states
            ):
                orders = curr_orders
                dfs_states = curr_dfs_states
                yield (curr_vertex, curr_dfs_states)


def bfs_component(
    graph: AdjList,
    start_vertex: int = 0,
    distance: int = 0,
    distances: list[int | float] | None = None,
    parents: list[int] | None = None,
) -> Iterator[tuple[int, BFSStates[list[int], list[int | float]]]]:
    if distances is None:
        num_of_V = len(graph)
        distances = [inf] * num_of_V
    if parents is None:
        num_of_V = len(graph)
        parents = [None] * num_of_V

    to_visit = deque()
    to_visit.append(start_vertex)
    distances[start_vertex] = distance
    distance += 1

    while len(to_visit) != 0:
        curr_vertex = to_visit.popleft()

        yield (curr_vertex, BFSStates(parents, distances))

        for nbr in graph[curr_vertex]:
            if distances[nbr] == inf:
                distances[nbr] = distance
                distance += 1
                parents[nbr] = curr_vertex
                to_visit.append(nbr)


def bfs(
    graph: AdjList, start_vertex: int = 0
) -> Iterator[tuple[int, BFSStates[list[int], list[int | float]]]]:

    distance = 0
    length = len(graph)
    distances = [inf] * length
    parents = [None] * length

    for i in range(length):
        if distances[i] == inf:
            for res in dfs_component(graph, i, distance, distances, parents):
                yield res
