"""
Detect Cycle in a Directed Graph

A directed graph contains a cycle if, during DFS, we encounter
a vertex that is already present in the current recursion path.

Idea:
1. Maintain two arrays:
   • visited -> whether a vertex has been visited before.
   • recSt   -> whether a vertex is currently in the recursion stack.
2. Run DFS from every unvisited vertex to handle disconnected components.
3. During DFS:
   • If a neighbour is unvisited, recursively visit it.
   • If a neighbour is already in the current recursion stack,
     a cycle exists.
4. Remove the current vertex from the recursion stack while backtracking.

Time Complexity:
    O(V + E)

Space Complexity:
    O(V)

where,
V = number of vertices
E = number of edges 

Note:
• This implementation uses DFS.
• `recSt` is different from `visited`:
    visited -> visited at any point in the traversal
    recSt   -> currently present in the active DFS path
"""

def dfsRec(adj, src, visited, recSt):
    visited[src] = True
    recSt[src] = True

    for neighbour in adj[src]:
        if not visited[neighbour] and dfsRec(adj, neighbour, visited, recSt):
            return True
        elif recSt[neighbour]:
            return True

    recSt[src] = False
    return False

def isCycle(adj): # using dfs considering we can have disconnected components as well
    visited = [False] * len(adj)
    recSt = [False] * len(adj)

    for vertex in range(len(adj)):
        if not visited[vertex]:
            if dfsRec(adj, vertex, visited, recSt):
                return True

    return False