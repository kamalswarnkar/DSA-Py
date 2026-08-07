"""
Count Connected Components in a Graph

A connected component is a maximal set of vertices such
that every pair of vertices is connected by a path.

Idea:
1. Maintain a visited array.
2. Iterate through every vertex.
3. If a vertex is unvisited:
   • Increment the component count.
   • Perform BFS from that vertex.
4. The total number of BFS traversals equals the
   number of connected components.

Time Complexity:
    O(V + E)

Space Complexity:
    O(V)

where,
V = number of vertices
E = number of edges

Note:
• This implementation works for undirected graphs.
• Every connected component is traversed exactly once.

Interview Notes:
• Number of connected components equals the number
  of BFS/DFS traversals started from unvisited vertices.
• The same approach works with DFS by replacing the queue
  with recursion (or an explicit stack).
"""

from collections import deque as dq

def bfs(adj, s, visited):
    q = dq()
    q.append(s)
    visited[s] = True

    while q:
        curr = q.popleft()

        for neighbour in adj[curr]:
            if not visited[neighbour]:
                q.append(neighbour)
                visited[neighbour] = True

def countConnectedComponents(adj):
    visited = [False] * len(adj)

    count = 0

    for vertex in range(len(adj)):
        if not visited[vertex]:
            count += 1
            bfs(adj, vertex, visited)

    return count