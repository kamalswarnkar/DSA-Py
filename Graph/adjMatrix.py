"""
Graph Representation using an Adjacency Matrix

An adjacency matrix is a V × V matrix where
matrix[u][v] indicates whether an edge exists
between vertices u and v.

Idea:
1. Create a V × V matrix initialized with 0.
2. For every edge (u, v):
   • Set matrix[u][v] = 1.
   • Set matrix[v][u] = 1 (for an undirected graph).
3. For a directed graph:
   • Set only matrix[u][v] = 1.

Time Complexity:
    Add Edge    : O(1)
    Remove Edge : O(1)
    Check Edge  : O(1)
    Print Graph : O(V²)

Space Complexity:
    O(V²)

where,
V = number of vertices

Note:
• This implementation represents an undirected graph.
• For a directed graph, set only matrix[u][v] = 1.
• Adjacency matrices are preferred for dense graphs.
"""

def createGraph(v):
    return [[0] * v for _ in range(v)]

def addEdge(adj, u, v):
    adj[u][v] = 1
    adj[v][u] = 1

def removeEdge(adj, u, v):
    adj[u][v] = 0
    adj[v][u] = 0

def hasEdge(adj, u, v):
    return adj[u][v] == 1

def printGraph(adj):
    for row in adj:
        print(*row)