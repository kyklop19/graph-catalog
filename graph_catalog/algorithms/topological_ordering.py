from algorithms.cycles import check_for_cycle_directed
from algorithms.searching import dfs
from constants import AdjList


def find_topological_ordering(graph: AdjList) -> list[int]:
    res = []

    if not check_for_cycle_directed:
        for curr_vertex, dfs_states in dfs(graph):
            if dfs_states.closing_orders[curr_vertex] != -1:
                res.append(curr_vertex)

    res.reverse()
    return res
