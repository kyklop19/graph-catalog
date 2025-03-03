from constants import AdjList
from searching import dfs


def check_for_cycle_undirected(graph: AdjList) -> bool:
    has_cycle = False
    for curr_vertex, orders, __ in dfs(graph):
        for nbr in graph[curr_vertex]:
            if orders[nbr] != -1:
                has_cycle = True
                break
        if has_cycle:
            break
    return has_cycle


def check_for_cycle_directed(graph: AdjList) -> bool:
    pass
