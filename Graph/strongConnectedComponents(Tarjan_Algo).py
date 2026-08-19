"""
Finding Strongly Connected Components (SCCs) in a Directed Graph
using Tarjan's Algorithm (DFS based)

Strongly Connected Component:
    A maximal set of vertices in a directed graph such that
    every vertex is reachable from every other vertex.

Idea:
1. Perform DFS and assign every vertex a discovery time.
2. Maintain `low[u]`, the earliest discovered vertex reachable
   from u while considering vertices currently in the DFS stack.
3. Push every visited vertex onto a stack.
4. For every edge u → v:
   • If v is unvisited, recursively visit v and update low[u].
   • If v is currently in the stack, update low[u] using disc[v].
5. If low[u] == disc[u], then u is the root of an SCC.
6. Pop vertices from the stack until u is removed. All popped
   vertices belong to the same SCC.

Time Complexity:
    O(V + E)

Space Complexity:
    O(V)

where,
V = number of vertices
E = number of edges

Note:
• Tarjan's Algorithm uses a single DFS traversal.
• `disc[u]` represents the discovery time of vertex u.
• `low[u]` represents the earliest discovered vertex reachable
  from u while staying within the currently active DFS stack.
• `inStack[u]` tells whether u is currently present in the stack.
"""

def totalStrongComponents(adj):
    n = len(adj)

    disc = [-1] * n
    low = [-1] * n
    par = [-1] * n
    inStack = [False] * n
    stack = []

    count = 0
    timer = 0

    def dfs(u):
        nonlocal timer, count

        disc[u] = low[u] = timer
        timer += 1

        stack.append(u)
        inStack[u] = True

        for v in adj[u]:
            if disc[v] == -1: # Tree edge: v is unvisited
                dfs(v)

                low[u] = min(low[u], low[v])

            elif inStack[v]: # Back edge: v is already visited and still active in stack
                low[u] = min(low[u], disc[v])

            # Cross/Forward edge:
            # v is visited but no longer in the stack, so it is ignored.

        if low[u] == disc[u]:
            while True:
                v = stack.pop()
                inStack[v] = False

                if v == u:
                    break
            
            count += 1

    for vertex in range(n):
        if disc[vertex] == -1:
            dfs(vertex)

    return count