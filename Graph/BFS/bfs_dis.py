"""
Breadth First Search (BFS) for a Disconnected Graph

Breadth First Search (BFS) visits vertices level by level.
For a disconnected graph, a single BFS call can only
traverse one connected component.

Idea:
1. Maintain a visited array.
2. Iterate through every vertex.
3. If a vertex is unvisited, perform BFS from it.
4. Repeat until every connected component has been visited.

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

from collections import deque as dq

def bfs(adj, s, visited):
    q = dq()
    q.append(s)
    visited[s] = True

    while q:
        curr = q.popleft()
        print(curr, end=" ")

        for neighbour in adj[curr]:
            if not visited[neighbour]:
                q.append(neighbour)
                visited[neighbour] = True

def bfsDisconnected(adj):
    visited = [False] * len(adj)

    for vertex in range(len(adj)):
        if not visited[vertex]:
            bfs(adj, vertex, visited)