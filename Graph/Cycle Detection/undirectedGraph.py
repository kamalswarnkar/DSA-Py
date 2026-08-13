"""
Detect Cycle in an Undirected Graph

A cycle exists if, during DFS, we encounter an already visited
neighbour that is not the parent of the current vertex.

Idea:
1. Maintain a visited array.
2. Run DFS from every unvisited vertex to handle disconnected graphs.
3. During DFS:
   • If a neighbour is unvisited, recursively visit it.
   • If a neighbour is already visited and is not the parent,
     a cycle exists.

Time Complexity:
    O(V + E)

Space Complexity:
    O(V)

where,
V = number of vertices
E = number of edges

Note:
• This implementation is for undirected graphs.
• The parent check is necessary because every undirected edge
  appears in both vertices' adjacency lists.
"""

def dfsRec(adj, src, visited, parent):
    visited[src] = True

    for neighbour in adj[src]:
        if not visited[neighbour]:
            if dfsRec(adj, neighbour, visited, src):
                return True
        elif neighbour != parent:
            return True

    return False

def isCycle(adj): # using dfs considering we can have disconnected components as well
    visited = [False] * len(adj)

    for vertex in range(len(adj)):
        if not visited[vertex]:
            if dfsRec(adj, vertex, visited, -1):
                return True

    return False