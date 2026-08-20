"""
Minimum Spanning Tree (MST) using Kruskal's Algorithm

A Minimum Spanning Tree is a spanning tree of a connected,
weighted, undirected graph with the minimum possible total
edge weight.

Properties:
• An MST contains all V vertices.
• An MST contains exactly V - 1 edges.
• The graph must be connected, weighted, and undirected.
• Kruskal's Algorithm is a greedy algorithm.

Idea:
1. Sort all edges in increasing order of weight.
2. Initialize an empty MST and total weight as 0.
3. Process edges in increasing order of weight.
4. If adding an edge does not create a cycle:
   • Add the edge to the MST.
   • Add its weight to the total.
5. Stop when the MST contains V - 1 edges.

Cycle Detection:
    Disjoint Set Union (DSU) / Union-Find is used to determine
    whether adding an edge creates a cycle.

Time Complexity:
    O(E log E)

Space Complexity:
    O(V + E)

where,
V = number of vertices
E = number of edges

Note:
• Kruskal's Algorithm processes edges globally in increasing
  order of weight.
• DSU efficiently detects whether two vertices already belong
  to the same connected component.
• If both endpoints of an edge belong to the same component,
  adding the edge would create a cycle, so the edge is skipped.
"""

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, rank, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x == y:
        return False

    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

    return True

def MST(adjM):
    n = len(adjM)

    parent = list(range(n))
    rank = [0] * n
    res, count = 0, 0

    edges = []

    for row in range(n):
        for col in range(row + 1, n):
            if adjM[row][col] != 0 and adjM[row][col] < float("inf"):
                edges.append([row, col, adjM[row][col]])

    edges.sort(key=lambda e : e[2])

    for u, v, weight in edges:
        if union(parent, rank, u, v):
            res += weight
            count += 1

            if count == n - 1:
                break

    if count != n - 1:
        return None # graph is disconnected
    
    return None if count != n - 1 else res
