from algorithms.searching import dfs
from constants import AdjList


def count_components(graph: AdjList) -> int:
    """Count the number of components in an undirected graph

    Args:
        graph (AdjList): Undirected graph represented as adjacency list

    Returns:
        int: Number of components in the graph
    """

    num_of_components = 0

    for curr_vertex, dfs_states in dfs(graph):
        if dfs_states.parents[curr_vertex] is None:
            num_of_components += 1

    return num_of_components


def divide_into_components(graph: AdjList) -> list[int]:
    """Find for each vertex a component in which the vertex is contained

    Args:
        graph (AdjList): Undirected graph represented as adjacency list

    Returns:
        list[int]: List where each index represents vertex and each element is an index of a component
    """
    num_of_V = len(graph)
    res = [-1] * num_of_V

    component_num = -1

    for curr_vertex, dfs_states in dfs(graph):
        if dfs_states.parents[curr_vertex] is None:
            component_num += 1
        res[curr_vertex] = component_num

    return res
