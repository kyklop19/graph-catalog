from algorithms.searching import dfs
from constants import AdjList


def has_cycle(graph: AdjList) -> bool:
    has_cycle = False
    for curr_vertex, dfs_states in dfs(graph):
        for nbr, __ in graph[curr_vertex]:
            if (
                dfs_states.opening_orders[nbr] != -1
                and dfs_states.closing_orders[nbr] == -1
            ):
                has_cycle = True
                break
        if has_cycle:
            break
    return has_cycle
