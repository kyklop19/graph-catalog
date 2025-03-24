from collections import deque, namedtuple
from enum import Flag, auto
from math import inf
from typing import Iterator

from graph_catalog.constants import AdjList

DFSStates = namedtuple("DFSStates", ("parents", "opening_orders", "closing_orders"))
BFSStates = namedtuple("BFSStates", ("parents", "distances"))


class DFSOrder(Flag):
    PREORDER = auto()
    POSTORDER = auto()


def _dfs_component(
    graph: AdjList,
    start_vertex: int,
    orders: tuple[int, int],
    dfs_states: DFSStates[list[int | None], list[int], list[int]],
    search_order: DFSOrder,
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

            if DFSOrder.PREORDER in search_order:
                yield (
                    curr_vertex,
                    (opening_order, closing_order),
                    DFSStates(parents, opening_orders, closing_orders),
                )

            for nbr, __ in reversed(graph[curr_vertex]):
                if opening_orders[nbr] == -1:
                    parents[nbr] = curr_vertex
                    to_visit.append(nbr)

        elif closing_orders[curr_vertex] == -1:
            closing_orders[curr_vertex] = closing_order
            closing_order += 1
            to_visit.pop()

            if DFSOrder.POSTORDER in search_order:
                yield (
                    curr_vertex,
                    (opening_order, closing_order),
                    DFSStates(parents, opening_orders, closing_orders),
                )
        else:
            to_visit.pop()


def dfs_component(
    graph: AdjList,
    start_vertex: int = 0,
    search_order: DFSOrder = DFSOrder.PREORDER,
) -> Iterator[tuple[int, DFSStates[list[int | None], list[int], list[int]]]]:
    length = len(graph)
    orders = (0, 0)
    dfs_states = DFSStates(
        [None] * length,
        [-1] * length,
        [-1] * length,
    )

    for curr_vertex, __, curr_dfs_states in _dfs_component(
        graph, start_vertex, orders, dfs_states, search_order
    ):
        yield (curr_vertex, curr_dfs_states)


def dfs(
    graph: AdjList,
    start_vertex: int = 0,
    search_order: DFSOrder = DFSOrder.PREORDER,
) -> Iterator[tuple[int, DFSStates[list[int | None], list[int], list[int]]]]:
    """Iterates over the graph's vertices in DFS manner and yields current vertex and state

    Args:
        graph (AdjList): Graph as `AdjList`
        start_vertex (int, optional): _description_. Defaults to 0.

    Yields:
        Iterator[tuple[int, DFSStates[list[int | None], list[int], list[int]]]]: _description_
    """
    length = len(graph)
    orders = (0, 0)
    dfs_states = DFSStates(
        [None] * length,
        [-1] * length,
        [-1] * length,
    )

    for curr_vertex, curr_orders, curr_dfs_states in _dfs_component(
        graph, start_vertex, orders, dfs_states, search_order
    ):
        orders = curr_orders
        dfs_states = curr_dfs_states
        yield (curr_vertex, curr_dfs_states)

    for i in range(length):
        if dfs_states.opening_orders[i] == -1:
            for curr_vertex, curr_orders, curr_dfs_states in _dfs_component(
                graph, i, orders, dfs_states, search_order
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
    to_visit_next = deque()
    distances[start_vertex] = distance
    distance += 1

    while len(to_visit) != 0:
        curr_vertex = to_visit.popleft()

        yield (curr_vertex, BFSStates(parents, distances))

        for nbr, __ in graph[curr_vertex]:
            if distances[nbr] == inf:
                distances[nbr] = distance
                parents[nbr] = curr_vertex
                to_visit_next.append(nbr)

        if len(to_visit) == 0:
            to_visit = to_visit_next
            to_visit_next = deque()
            distance += 1


def bfs(
    graph: AdjList, start_vertex: int = 0
) -> Iterator[tuple[int, BFSStates[list[int], list[int | float]]]]:

    distance = 0
    length = len(graph)
    distances = [inf] * length
    parents = [None] * length

    for i in range(length):
        if distances[i] == inf:
            for res in bfs_component(graph, i, distance, distances, parents):
                yield res
