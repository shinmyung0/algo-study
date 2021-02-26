import math
from collections import defaultdict


def dijkstra(adj_matrix):
    result = defaultdict(int)
    return result


def shortest_path_to(path_table, dest_node):
    return path_table[dest_node]


def test_dijkstra():

    test_matrix = [[0, 1, 3, 0], [0, 0, 1, 5], [0, 0, 0, 1], [0, 0, 0, 0]]
    start_node = 0
    dest_node = 3
    shortest_paths_table = dijkstra(0)

    result = shortest_paths_table[3]

    assert result == 3
