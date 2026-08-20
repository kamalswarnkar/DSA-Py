"""
Minimum Spanning Tree (MST) using Prim's Algorithm


A Minimum Spanning Tree is a spanning tree of a connected,
weighted, undirected graph with the minimum possible total
edge weight.


Properties:
• An MST contains all V vertices.
• An MST contains exactly V - 1 edges.
• The graph must be connected, weighted, and undirected.
• Prim's Algorithm is a greedy algorithm.


Idea:
1. Maintain a set of vertices already included in the MST.
2. Maintain a key value for every vertex.
   • key[v] = minimum edge weight connecting v to the MST.
3. Initialize all key values to INF.
4. Set the key of the starting vertex to 0 so that it is
   selected first.
5. Repeatedly select the unvisited vertex with the minimum key.
6. Add it to the MST and update the key values of its
   adjacent vertices.
7. The sum of the selected key values gives the total
   weight of the MST.


Time Complexity: O(V²)
Space Complexity: O(V)


where,
V = number of vertices


Note:
• This implementation uses an adjacency matrix.
• A value of 0 represents the absence of an edge.
• For a connected graph, every vertex will eventually
  be included in the MST.
• `key[v]` stores the cheapest edge currently connecting
  vertex v to the growing MST.
"""

def MST(adjM):# we are using adjacency matric because it will easily tell if edge exist and if yes then what's the weight
    n = len(adjM)
    key = [float("inf") for _ in range(n)]
    key[0] = 0 # start from vertex 0
    res = 0
    mstSet = [False] * n

    for _ in range(n):
        u = -1

        for i in range(n): # Select the unvisited vertex with minimum key value.
            if not mstSet[i] and (u == -1 or key[i] < key[u]):
                u = i

        mstSet[u] = True
        res += key[u]

        for v in range(n): # Update key values of adjacent unvisited vertices.
            edge = adjM[u][v]
            if not mstSet[v] and edge != 0 and edge < key[v]:
                key[v] = edge

    return res