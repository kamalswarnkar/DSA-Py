"""
Depth First Search (DFS) for a Disconnected Graph

A single DFS traversal visits only the connected
component containing the source vertex.

To traverse a disconnected graph:
1. Maintain a visited array.
2. Iterate through every vertex.
3. If a vertex is unvisited, start a DFS from it.
4. Repeat until all connected components are visited.

Time Complexity:
    O(V + E)

Space Complexity:
    O(V)

where,
V = number of vertices
E = number of edges

Note:
• Works for both directed and undirected graphs.
• Every vertex is visited exactly once.
• Every edge is processed exactly once.
"""

def dfsRec(adj, s, visited):
    visited[s] = True
    print(s, end=" ")

    for neighbour in adj[s]:
        if not visited[neighbour]:
            dfsRec(adj, neighbour, visited)

def dfsDisconnected(adj, s):
    visited = [False] * len(adj)

    for vertex in range(len(adj)):
        if not visited[vertex]:
            dfsRec(adj, vertex, visited)