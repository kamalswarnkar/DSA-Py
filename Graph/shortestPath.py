"""
Shortest Path in an Unweighted Graph

Find the shortest distance from a given source vertex to
every other vertex in an unweighted graph.

Idea:
1. Initialize the distance of every vertex to INT_MAX.
2. Set the source distance to 0.
3. Perform BFS from the source.
4. Whenever an unvisited neighbour is found, its shortest
   distance is:
       dist[neighbour] = dist[curr] + 1
5. BFS guarantees that vertices are reached in increasing
   order of their distance from the source.

Time Complexity:
    O(V + E)

Space Complexity:
    O(V)

where,
V = number of vertices
E = number of edges

Note:
• BFS gives the shortest path in an unweighted graph.
• Each edge is considered to have a weight of 1.
• If a vertex remains at INT_MAX, it is unreachable
  from the source.
"""

from collections import deque as dq

INF = float("inf")

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def bfs(adj, src, dist):
    q = dq([src])
    dist[src] = 0

    while q:
        curr = q.popleft()

        for neighbour in adj[curr]:
            if dist[neighbour] == INF:
                dist[neighbour] = dist[curr] + 1
                q.append(neighbour)