"""
Graph Representation using an Adjacency List

An adjacency list stores, for every vertex, the list of
vertices directly connected to it.

Idea:
1. Create a list of adjacency lists.
2. For every edge (u, v):
   • Add v to u's list.
   • Add u to v's list (for an undirected graph).
3. For a directed graph:
   • Add only (u → v).

Time Complexity:
    Add Edge    : O(1); with assumption
    Add Edge    : O(deg(u) + deg(v)); without assumption
    Print Graph : O(V + E)

Space Complexity:
    O(V + E)

where,
V = number of vertices
E = number of edges

Note:
• This implementation represents an undirected graph.
• For a directed graph, insert only (u → v).
"""

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

    """
    Assumption: There are no duplicate edges in the input, so we skip this check below.
    if v not in adj[u]:
        adj[u].append(v)
    if u not in adj[v]:
        adj[v].append(u)
    """

def printGraph(adj):
    for u, neighbours in enumerate(adj):
        print(f"{u} -> {neighbours}")