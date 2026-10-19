"""
Kruskal's Algorithm Using Disjoint Set Union (DSU)

Problem:
    Find the total weight of a Minimum Spanning Tree (MST)
    in a weighted, undirected graph.

Approach:
    1. Sort all edges in non-decreasing order of weight.
    2. Use DSU with path compression and union by rank.
    3. Add an edge if its endpoints belong to different sets.
    4. Stop after selecting N - 1 edges.

Time Complexity:  O(E log E + E * α(N))
Space Complexity: O(N), excluding the input edges.
"""

def kruskal(edges, n):
    # Each edge is represented as [u, v, weight]

    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    def find(x):
        if parent[x] == x:
            return x

        parent[x] = find(parent[x]) # path compression

        return parent[x]

    def union(x, y):
        x_rep = find(x)
        y_rep = find(y)

        if x_rep == y_rep:
            return

        # union by rank
        if rank[x_rep] > rank[y_rep]:
            parent[y_rep] = x_rep
        elif rank[x_rep] < rank[y_rep]:
            parent[x_rep] = y_rep
        else:
            parent[y_rep] = x_rep
            rank[x_rep] += 1

    edges.sort(key = lambda e : e[2])
    res, s = 0, 0

    for e in edges:
        u, v, w = e
        us = find(u)
        vs = find(v)

        if us != vs:
            res += w
            union(us, vs)
            s += 1

        if s == n - 1:
            break

    return res
