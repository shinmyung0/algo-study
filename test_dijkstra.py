import math


def init_shortest_paths(n, source_node):
    shortest_paths = {}
    for i in range(n):
        shortest_paths[i] = (math.inf, None)

    shortest_paths[source_node] = (0, None)
    return shortest_paths


def dijkstra(adj_matrix, source_node):
    """
    Given adj_matrix and starting source node
    return shortest paths table from source node using Dijkstra's algorithm
    """
    # init shortest paths table and unvisited table
    N = len(adj_matrix)
    shortest_paths = init_shortest_paths(N, source_node)

    return shortest_paths


def shortest_path_to(path_table, dest_node):
    return path_table[dest_node]


def shortest_path_str(source_node, dest_node, path_table):
    result = "{}".format(dest_node)
    curr = path_table[dest_node][1]
    while curr != None:
        result += "<-{}".format(curr)
        curr = path_table[curr][1]
    return result


def shortest_path_dist(dest_node, path_table):
    return path_table[dest_node][0]


def test_dijkstra():

    test_matrix = [[0, 1, 3, 0], [0, 0, 1, 5], [0, 0, 0, 1], [0, 0, 0, 0]]
    start_node = 0
    dest_node = 3
    shortest_paths_table = dijkstra(test_matrix, start_node)

    result = shortest_path_dist(dest_node, shortest_paths_table)

    assert result == 3
    result = shortest_path_str(0, 3, shortest_paths_table)
    assert result == "3<-2<-1<-0"
