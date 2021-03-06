import math

# test graphs
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return "Node " + str(self.val)


nodes = []
for i in range(5):
    nodes.append(Node(i))

nodes[0].add_child(nodes[1])
nodes[0].add_child(nodes[2])
nodes[1].add_child(nodes[0])
nodes[1].add_child(nodes[3])
nodes[2].add_child(nodes[3])
nodes[3].add_child(nodes[4])


g1_oop = nodes[0]
g1_adj_list = [[1, 2], [0, 3], [3], [4], []]
g1_adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
]

# end test graphs


def dfs_visit_order_adj_list(start_node, adj_list):
    visited = set()
    to_visit = [start_node]

    traverse_path = []

    while len(to_visit) != 0:
        curr = to_visit.pop()

        if curr not in visited:
            visited.add(curr)

            traverse_path.append(curr)

            children = adj_list[curr]
            for child in children:
                if child not in visited:
                    to_visit.append(child)
    return traverse_path


def dfs_visit_order_adj_matrix(start_node, adj_matrix):
    visited = set()
    to_visit = [start_node]

    traverse_path = []

    while to_visit:
        curr = to_visit.pop()

        if curr not in visited:
            visited.add(curr)

            traverse_path.append(curr)

            edges = adj_matrix[curr]

            # this will take |V| for every V
            # for adj matrix
            for n, w in enumerate(edges):
                if w > 0 and n not in visited:
                    to_visit.append(n)

    return traverse_path


def dfs_visit_order_oop(head):
    visited = set()
    to_visit = [head]

    traverse_order = []

    while len(to_visit) != 0:
        # consume as stack
        curr = to_visit.pop()

        if curr.val not in visited:
            visited.add(curr.val)

            # do some work
            traverse_order.append(curr.val)

            # add children onto to_visit
            for node in curr.children:
                if node.val not in visited:
                    to_visit.append(node)

    return traverse_order


def dfs_visited_order_oop_recursive(head):
    visited = set()

    def helper(node, visited):
        if node.val in visited:
            return []
        visited.add(node.val)
        visited_from_here = [node.val]
        for child in node.children:
            visited_from_here += helper(child, visited)
        return visited_from_here

    return helper(head, visited)


def test_dfs():

    visit_answer1 = [0, 2, 3, 4, 1]
    visit_answer2 = [0, 1, 3, 4, 2]

    result = dfs_visit_order_oop(g1_oop)
    assert result == visit_answer1

    result = dfs_visited_order_oop_recursive(g1_oop)
    assert result == visit_answer2

    result = dfs_visit_order_adj_list(0, g1_adj_list)
    assert result == visit_answer1

    result = dfs_visit_order_adj_matrix(0, g1_adj_matrix)
    assert result == visit_answer1


def bfs_oop(head):
    visited = set()
    to_visit = [head]

    traverse_path = []
    while to_visit:
        curr = to_visit.pop(0)
        if curr.val not in visited:
            visited.add(curr.val)

            traverse_path.append(curr.val)

            for child in curr.children:
                if child.val not in visited:
                    to_visit.append(child)
    return traverse_path


def recursive_bfs_oop(head):
    seen_set = set()
    initial_queue = [head]
    seen_set.add(head.val)

    def helper(to_visit, seen):
        if len(to_visit) == 0:
            return []

        node = to_visit.pop(0)
        traversed = [node.val]
        for child in node.children:
            if child.val not in seen:
                # when children are added they are considered seen
                # so no child that has already been added will get added again
                seen.add(child.val)
                to_visit.append(child)
        return traversed + helper(to_visit, seen)

    return helper(initial_queue, seen_set)


def test_bfs():
    traverse_answer1 = [0, 1, 2, 3, 4]

    result = bfs_oop(g1_oop)
    assert result == traverse_answer1

    result = recursive_bfs_oop(g1_oop)
    assert result == traverse_answer1
