"""
Detect Cycle Using Disjoint Set Union (DSU)

Problem:
    Determine whether an undirected graph contains a cycle.

Approach:
    1. Initialize every vertex as its own set.
    2. Process each undirected edge only once.
    3. If both endpoints have the same representative,
       the edge creates a cycle.
    4. Otherwise, merge their sets using union by rank
       and path compression.

Time Complexity:  O(V + E * α(V)) amortized.
Space Complexity: O(V) for the parent and rank arrays.
"""

def detectCycle(V, adj):
    parent = list(range(V))
    rank = [0] * V

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]

    def union(x, y):
        x_rep, y_rep = find(x), find(y)

        if x_rep == y_rep:
            return True

        if rank[x_rep] > rank[y_rep]:
            parent[y_rep] = x_rep
        elif rank[x_rep] < rank[y_rep]:
            parent[x_rep] = y_rep
        else:
            parent[y_rep] = x_rep
            rank[x_rep] += 1

        return False

    for u in range(V):
        for v in adj[u]:
            if u < v:
                if union(u, v):
                    return True

    return False