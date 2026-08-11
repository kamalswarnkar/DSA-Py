"""
Count Connected Components in a Graph

A connected component is a maximal set of vertices where
every pair of vertices is connected by a path.

Idea:
1. Maintain a visited array.
2. Iterate through every vertex.
3. If a vertex is unvisited, start DFS from it.
4. Increment the count for every new DFS traversal.

Time Complexity:
    O(V + E)

Space Complexity:
    O(V)

where,
V = number of vertices
E = number of edges

Note:
• This implementation uses DFS.
• Every connected component is traversed exactly once.
• This implementation assumes an undirected graph.
"""

def dfsRec(adj, s, visited):
    visited[s] = True

    for neighbour in adj[s]:
        if not visited[neighbour]:
            dfsRec(adj, neighbour, visited)

def countConnectedComponents(adj):
    visited = [False] * len(adj)

    count = 0

    for vertex in range(len(adj)):
        if not visited[vertex]:
            count += 1
            dfsRec(adj, vertex, visited)

    return count