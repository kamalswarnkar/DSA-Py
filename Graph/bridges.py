"""
Finding Bridges in an Undirected Graph

A Bridge is an edge whose removal increases the number of
connected components of the graph.

Idea:
1. Perform DFS and assign every vertex a discovery time.
2. Maintain `low[u]`, the earliest discovered vertex reachable
   from the subtree of u using tree edges and at most one back edge.
3. For every DFS tree edge u — v:
   • If low[v] > disc[u], then u — v is a bridge.
4. Process every unvisited vertex so that disconnected graphs
   are also handled.

Time Complexity:
    O(V + E)

Space Complexity:
    O(V)

where,
V = number of vertices
E = number of edges

Note:
• This implementation is for an undirected graph.
• `disc[u]` represents the discovery time of vertex u.
• `low[u]` represents the earliest discovered vertex reachable
  from the subtree rooted at u.
• Unlike articulation points, bridges have no special root case.
"""

def bridges(adj):
    n = len(adj)

    disc = [-1] * n # discovery time of each vertex
    low = [-1] * n # earliest discovered vertex reachable from u's subtree
    par = [-1] * n # parent of each vertex in the DFS tree
    bridge = []

    timer = 0

    def dfs(u):
        nonlocal timer

        disc[u] = low[u] = timer
        timer += 1

        children = 0

        for v in adj[u]:
            if disc[v] == -1: # tree edge
                par[v] = u

                dfs(v)

                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    bridge.append(f"{u} --- {v}")

            elif v != par[u]: # back edge
                low[u] = min(low[u], disc[v])

    for vertex in range(n):
        if disc[vertex] == -1:
            dfs(vertex)

    return bridge