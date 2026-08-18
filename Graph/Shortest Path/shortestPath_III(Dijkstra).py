"""
Shortest Path in a Weighted Undirected Graph using Dijkstra's Algorithm

Find the shortest distance from a given source vertex to
every other vertex in a weighted graph.

Idea:
1. Initialize the distance of every vertex to INF.
2. Set the source vertex distance to 0.
3. Repeatedly select the unfinished vertex with the
   minimum distance.
4. Mark the selected vertex as finished.
5. Relax all its adjacent vertices:
       dist[v] = min(dist[v], dist[u] + weight(u, v))
6. Repeat until all vertices are processed.

Time Complexity:
    O(V²)

Space Complexity:
    O(V)

where,
V = number of vertices

Note:
• This implementation uses an adjacency matrix.
• Dijkstra's Algorithm works with non-negative edge weights.
• A finished vertex has its shortest distance finalized.
"""

def dijkstra(adjM, src):
    n = len(adjM) # no. of vertices

    dist = [float("inf") for _ in range(n)]
    finished = [False] * n

    dist[src] = 0

    for _ in range(n - 1):
        u = -1
        for i in range(n):
            if not finished[i] and (u == -1 or dist[i] < dist[u]):
                u = i

        finished[u] = True

        for v in range(n):
            if not finished[v] and adjM[u][v] != 0:
                dist[v] = min(dist[v], dist[u] + adjM[u][v])

    return dist