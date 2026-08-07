"""
Breadth First Search (BFS) of a Graph

Breadth First Search (BFS) visits vertices level by level,
starting from a given source vertex.

Idea:
1. Mark the source vertex as visited.
2. Insert it into a queue.
3. Repeatedly:
   • Remove the front vertex.
   • Visit all its unvisited neighbours.
   • Mark them visited and enqueue them.

Time Complexity:
    O(V + E)

Space Complexity:
    O(V)

where,
V = number of vertices
E = number of edges

Note:
• Works on both directed and undirected graphs.
• This implementation traverses only the connected
  component containing the source vertex.
• For a disconnected graph, run BFS from every
  unvisited vertex.
"""

from collections import deque as dq

def bfs(adj, s):
    visited = [False] * len(adj)
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