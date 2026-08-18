"""
Finding Articulation Points in an Undirected Graph

An Articulation Point is a vertex whose removal increases
the number of connected components of the graph.

Idea:
1. Perform DFS and assign every vertex a discovery time.
2. Maintain `low[u]`, the earliest discovered vertex that can
   be reached from the subtree of u using tree edges and at
   most one back edge.
3. For every DFS child v of u:
   • If u is not the root and low[v] >= disc[u], then u is
     an articulation point.
   • If u is the root and it has more than one DFS child,
     then u is an articulation point.
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
• A DFS root is an articulation point only if it has more than
  one DFS child.
"""

def articulationPoint(adj):
    n = len(adj)

    disc = [-1] * n # discovery time of all vertices
    low = [-1] * n  # earliest discovered vertex from the subtree rooted at respective vertex
    par = [-1] * n # parent of all vertices
    ap = [False] * n # marks whether each vertex is an articulation point
    
    timer = 0

    def dfs(u):
        nonlocal timer

        disc[u] = low[u] = timer
        timer += 1

        children = 0

        for v in adj[u]:
            if disc[v] == -1: # tree edge
                par[v] = u
                children += 1

                dfs(v)

                low[u] = min(low[u], low[v])

                if par[u] != -1 and low[v] >= disc[u]: # u is not root and v cannot reach an ancestor of u
                    ap[u] = True

            elif v != par[u]: # back edge
                low[u] = min(low[u], disc[v])

        if par[u] == -1 and children > 1: # root with more than one DFS child
            ap[u] = True

    for vertex in range(n):
        if disc[vertex] == -1:
            dfs(vertex)

    return [vertex for vertex in range(n) if ap[vertex]]