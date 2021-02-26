# Dijkatra's Algorithm

Dijkstra's Algorithm is used for finding shortest paths from a source node to all other nodes in a graph.

The algorithm works for all graphs:

- undirected / directed : this is true because undirected is just a special case of directed where all nodes have bidirectional edges
- connected / disconnected : this is true because disconnected graph means there will simply be vertices which are not reachable from a given source node. Distance for these unreachable nodes from a source node can simply by infinity.

The main idea is:

BFS + priority queue for the unvisited queue ordered by shortest distance

# Pseudocode

# Check implementation

```
> pytest test_dijkstra.py
```