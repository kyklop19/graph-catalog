from collections import deque
from enum import IntEnum

from constants import AdjList


class SearchState(IntEnum):
    UNVISITED = 0
    OPENED = 1
    CLOSED = 2


def dfs(graph: AdjList, start_vertex: int = 0):

    length = len(graph)
    states = [SearchState.UNVISITED] * length
    parents = [None] * length

    for i in range(length):
        if states[i] is SearchState.UNVISITED:
            for res in dfs_component(graph, i, states, parents):
                yield res

    def dfs_component(graph, start_vertex, states, parents):
        to_visit = deque()
        to_visit.append(start_vertex)
        states[start_vertex] = SearchState.OPENED

        while len(to_visit) != 0:
            curr_vertex = to_visit.pop()

            yield curr_vertex, states, parents

            for nbr in graph[curr_vertex]:
                if states[nbr] is SearchState.UNVISITED:
                    to_visit.append(nbr)
                    states[nbr] = SearchState.OPENED
