"""
Depth First Search (DFS) of a Graph

Depth First Search (DFS) explores a path as far as possible
before backtracking to explore other paths.

Idea:
1. Mark the current vertex as visited.
2. Visit the current vertex.
3. Recursively visit every unvisited neighbour.
4. Backtrack when no unvisited neighbours remain.

Time Complexity:
    O(V + E)

Space Complexity:
    O(V)

where,
V = number of vertices
E = number of edges

Note:
• Works for both directed and undirected graphs.
• This implementation traverses only the connected
  component containing the source vertex.
• For a disconnected graph, run DFS from every
  unvisited vertex.
"""

def dfsRec(adj, s, visited):
    visited[s] = True
    print(s, end=" ")

    for neighbour in adj[s]:
        if not visited[neighbour]:
            dfsRec(adj, neighbour, visited)

def dfs(adj, s):
    visited = [False] * len(adj)
    dfsRec(adj, s, visited)