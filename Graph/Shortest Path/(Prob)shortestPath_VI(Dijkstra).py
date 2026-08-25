"""
Shortest Path in 1-2 Graph

Problem:
    Given a weighted undirected graph with V vertices numbered
    from 0 to V - 1, where every edge has a weight of either
    1 or 2, find the shortest distance from src to dest.

Idea:
1. Convert the edge list into an adjacency list.
2. Initialize the distance of every vertex as INF.
3. Set dist[src] = 0.
4. Use a min-heap to always process the vertex with the
   smallest known distance.
5. Relax all adjacent edges.
6. When dest is removed from the min-heap, its shortest
   distance has been finalized.

Algorithm:
    Dijkstra's Algorithm

Time Complexity:
    O((V + E) log V)

Space Complexity:
    O(V + E)

where,
V = number of vertices
E = number of edges

Note:
• All edge weights are positive (1 or 2), so Dijkstra's
  Algorithm can be used.
• The graph is undirected, so every edge is added in both
  directions.
• If dest is unreachable, return -1.
"""

import heapq

def shortestPath(V, src, dest, edges):
    adj = [[] for _ in range(V)]
    dist = [float("inf")] * V
    dist[src] = 0

    for e in edges: # Build adjacency list.
        u, v, w = e
        adj[u].append((v, w))
        adj[v].append((u, w))

    q = [(0, src)] # (distance, vertex)

    while q:
        d, u = heapq.heappop(q)

        if d != dist[u]:
            continue

        if u == dest:
            return d

        for v, w in adj[u]:
            new_dist = d + w

            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(q, (new_dist, v))

    return -1