"""
Shortest Path in a Directed and Weighted Graph using Bellman-Ford

Bellman-Ford finds the shortest distance from a given source
vertex to every other vertex.

It can handle:
• Directed graphs
• Positive edge weights
• Zero edge weights
• Negative edge weights
• Negative-weight cycle detection

Unlike Dijkstra's Algorithm, Bellman-Ford does not require
all edge weights to be non-negative.

Idea:
1. Initialize the source distance as 0 and all other distances
   as INF.
2. Relax every edge V - 1 times.
3. After V - 1 iterations, all shortest paths are finalized
   if the graph contains no negative-weight cycle.
4. Perform one additional relaxation pass:
   • If any distance can still be reduced, a negative-weight
     cycle exists.

Why V - 1 iterations?
    A simple shortest path can contain at most V - 1 edges.
    Therefore, after V - 1 complete relaxation passes, all
    shortest paths must have been found.

Time Complexity:
    Matrix Version : O(V³)
    Edge List Version: O(VE)

Space Complexity:
    Matrix Version : O(V²)
    Edge List Version: O(V + E)

where,
V = number of vertices
E = number of edges

Note:
• The order of edges does not matter.
• Bellman-Ford can detect negative-weight cycles.
• A negative-weight cycle makes a finite shortest path undefined.
• In the matrix version, 0 represents the absence of an edge,
  so zero-weight edges cannot be represented.
"""

def bellmanFord_I(adjM, src): # using adjacency matrix
    n = len(adjM)
    dist = [float("inf")] * n
    dist[src] = 0

    for _ in range(n - 1): # Relax all edges (n - 1) times
        updated = False

        for vertex in range(n):
            if dist[vertex] == float("inf"):
                continue

            for neighbour in range(n):
                weight = adjM[vertex][neighbour]
                if weight != 0 and dist[neighbour] > dist[vertex] + weight:
                    dist[neighbour] = dist[vertex] + weight
                    updated = True

        if not updated: # no relaxation, means shortest distances are already finalized
            break

    # check for a -ve  weight cycle:
    for vertex in range(n):
        if dist[vertex] == float("inf"):
            continue

        for neighbour in range(n):
            weight = adjM[vertex][neighbour]
            if weight != 0 and dist[neighbour] > dist[vertex] + weight:
                return None # -ve weight cycle exists

    return dist

def bellmanFord_II(edges, n, src):
    dist = [float("inf")] * n
    dist[src] = 0

    for _ in range(n - 1):
        updated = False
        for vertex, neighbour, weight in edges:
            if dist[vertex] != float("inf") and dist[neighbour] > dist[vertex] + weight:
                dist[neighbour] = dist[vertex] + weight
                updated = True

        if not updated:
            break

    for vertex, neighbour, weight in edges:
        if dist[vertex] != float("inf") and dist[neighbour] > dist[vertex] + weight:
            return None

    return dist