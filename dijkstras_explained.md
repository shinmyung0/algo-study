# Dijkatra's Algorithm

Dijkstra's Algorithm is used for finding shortest paths from a source node to all other nodes in a graph.

The algorithm works for all graphs:

- undirected / directed : this is true because undirected is just a special case of directed where all nodes have bidirectional edges
- connected / disconnected : this is true because disconnected graph means there will simply be vertices which are not reachable from a given source node. Distance for these unreachable nodes from a source node can simply by infinity.

The main idea is:

BFS + priority queue for the unvisited queue ordered by shortest distance

# Pseudocode


```
initialize shortest paths table where key is node id and value is (distance, predecessor)

source node entry should be (0, None)

all other node distances should be set to (infinity, None)

while there are unvisited nodes:
    get the current next node to visit based on lowest distance
    get the curr node neighbors
    for each neighbor
        calculate the total distance by adding entry in shortest path table and edge weight between the nodes
        if the new distance is less than the current entry
            update the shortest paths table = (new dist, curr_node)
    
    mark current node as visited
    
return shortest paths table


```

# Runtime analysis

Total runtime consists of

- visiting all nodes
    - O(|V|)
- visiting all edges
    - O(|E|)
- checking if the priority queue is empty
    - O(1)
- updating priority queue values when checking every neighbor 
    - O(|E|log|V|) if using min-heap priority queue
- finding a removing the next node lowest value
    - O(|V|log|V|)

For connected graphs generally |V| is dominated by |E|

So you can say O(|V|log|V|) is dominated by O(|E|log|V|)

which makes the runtime complexity O(|E|log|V|)

BUT you can use a special data structure called a fibonacci heap to reduce the runtime to O(|E| + |V|log|V|)


# Check implementation

```
> pytest test_dijkstra.py
```