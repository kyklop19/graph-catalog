from collections import deque
from enum import IntEnum

from constants import AdjList


class SearchState(IntEnum):
    UNVISITED = 0
    OPENED = 1
    CLOSED = 2


def dfs_component(
    graph: AdjList,
    start_vertex: int = 0,
    order: int = -1,
    orders: list[SearchState] | None = None,
    parents: list[int] | None = None,
):
    if orders is None:
        num_of_V = len(graph)
        orders = [-1] * num_of_V
    if parents is None:
        num_of_V = len(graph)
        parents = [None] * num_of_V

    to_visit = deque()
    to_visit.append(start_vertex)
    order += 1
    orders[start_vertex] = order

    while len(to_visit) != 0:
        curr_vertex = to_visit.pop()

        yield curr_vertex, orders, parents

        for nbr in graph[curr_vertex]:
            if orders[nbr] == -1:
                order += 1
                orders[nbr] = order
                to_visit.append(nbr)


def dfs(graph: AdjList, start_vertex: int = 0):

    order = -1
    length = len(graph)
    orders = [-1] * length
    parents = [None] * length

    for i in range(length):
        if orders[i] == -1:
            for res in dfs_component(graph, i, order, orders, parents):
                yield res
