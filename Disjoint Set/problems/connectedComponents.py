"""
Number of Connected Components Using DSU

Problem:
    Given an undirected graph with V vertices and a list of edges,
    count the number of connected components.

Approach:
    1. Initially, each vertex forms its own component.
    2. Process every edge using DSU.
    3. If an edge connects two different components, merge them
       and decrement the component count.
    4. Return the final count.

Time Complexity:  O(V + E * α(V)) amortized.
Space Complexity: O(V) auxiliary space.
"""

def countConnected(V, edges):
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

    count = V

    for edge in edges:
        u, v = edge

        if not union(u, v):
            count -= 1

    return count