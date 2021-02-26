import math


def dijkstra(adj_matrix):

    return None


def shortest_path_between(source_node, dest_node):
    return math.inf


def test_dijkstra():

    test_matrix = [[0, 1, 3, 0], [0, 0, 1, 5], [0, 0, 0, 1], [0, 0, 0, 0]]
    start_node = 0
    dest_node = 3
    shortest_paths = dijkstra(0)

    result = shortest_path_between(0, 3)

    assert result == 3
