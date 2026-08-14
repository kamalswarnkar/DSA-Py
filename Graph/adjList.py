"""
Graph Representation using an Adjacency List

An adjacency list stores, for every vertex, the list of
vertices directly connected to it.

This file supports:
1. Undirected graph representation.
2. Directed graph representation.
3. Indegree tracking for directed graphs.

Idea:
1. Create a list of adjacency lists.
2. For an undirected edge (u, v):
   • Add v to u's list.
   • Add u to v's list.
3. For a directed edge (u → v):
   • Add v to u's list.
   • Increment indegree[v].

Time Complexity:
    Add Undirected Edge : O(1); with assumption
    Add Directed Edge   : O(1)
    Print Graph         : O(V + E)

Space Complexity:
    O(V + E)

where,
V = number of vertices
E = number of edges

Note:
• Duplicate edges are assumed to be absent.
• For directed graphs, `indeg[v]` stores the number of
  incoming edges to vertex v.
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

def addDirectedEdge(adj, u, v, indeg): # for directed graph + indegree
    adj[u].append(v)
    indeg[v] += 1

def printGraph(adj):
    for u, neighbours in enumerate(adj):
        print(f"{u} -> {neighbours}")

"""
Example: Initializing an adjacency list and an indegree array.
"""

def main():
    v = 5 # lets take 5 vertices for this example
    adj = [[] for _ in range(v)]
    indeg = [0] * v

    addDirectedEdge(adj, 0, 2, indeg)
    addDirectedEdge(adj, 0, 3, indeg)
    addDirectedEdge(adj, 1, 3, indeg)
    addDirectedEdge(adj, 1, 4, indeg)
    addDirectedEdge(adj, 2, 3, indeg)

# main()
