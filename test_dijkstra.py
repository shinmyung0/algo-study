import math


def init_shortest_paths(n, source_node):
    shortest_paths = {}
    for i in range(n):
        shortest_paths[i] = (math.inf, None)

    shortest_paths[source_node] = (0, None)
    return shortest_paths


def get_next_unvisited(visited, shortest_paths):
    """
    Simple linear search to return next unvisited node with shortest path value
    If none exist, will return None

    CAN BE OPTIMIZED
    """
    min_dist = math.inf
    min_node = None
    for node_id in shortest_paths:
        dist = shortest_paths[node_id][0]
        if dist < min_dist and visited[node_id] == False:
            min_dist = dist
            min_node = node_id
    return min_node


def get_neighbors(adj_matrix, node_id):
    """
    Return list of indices with positive weights

    CAN BE OPTIMIZED
    """
    result = []
    for i in range(len(adj_matrix[node_id])):
        if adj_matrix[node_id][i] > 0:
            result.append(i)
    return result


def dijkstra(adj_matrix, source_node):
    """
    Given adj_matrix and starting source node
    return shortest paths table from source node using Dijkstra's algorithm
    """
    # init shortest paths table and unvisited table
    N = len(adj_matrix)
    shortest_paths = init_shortest_paths(N, source_node)

    visited = [False] * N

    # while there are still unvisited nodes
    while False in visited:
        curr_node = get_next_unvisited(visited, shortest_paths)
        curr_dist = shortest_paths[curr_node][0]
        neighbors = get_neighbors(adj_matrix, curr_node)
        # for each neighbor

        for n in neighbors:
            edge_weight = adj_matrix[curr_node][n]
            # if the curr_dist + weight is less than what's
            # already in the shortest path entries for that neighbor
            # then update the shortest path entry value
            curr_entry = shortest_paths[n][0]
            if curr_dist + edge_weight < curr_entry:
                shortest_paths[n] = (curr_dist + edge_weight, curr_node)
        visited[curr_node] = True

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
