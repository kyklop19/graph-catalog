from algorithms.searching import dfs
from constants import AdjList


def get_num_of_components(graph: AdjList) -> int:

    num_of_components = 0

    for curr_vertex, dfs_states in dfs(graph):
        if dfs_states.parents[curr_vertex] is None:
            num_of_components += 1

    return num_of_components


def divide_into_components(graph: AdjList) -> list[int]:
    num_of_V = len(graph)
    res = [-1] * num_of_V

    component_num = -1

    for curr_vertex, dfs_states in dfs(graph):
        if dfs_states.parents[curr_vertex] is None:
            component_num += 1
        res[curr_vertex] = component_num

    return res
