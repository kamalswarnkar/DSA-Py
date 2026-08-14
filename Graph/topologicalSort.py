"""
Topological Sort using Kahn's Algorithm (BFS based)

Topological Sort is a linear ordering of the vertices of a
Directed Acyclic Graph (DAG) such that for every directed edge
u → v, vertex u appears before vertex v.

Idea:
1. Store the indegree of every vertex.
2. Add all vertices with indegree 0 to a queue.
3. Remove a vertex from the queue and add it to the result.
4. Decrease the indegree of all its neighbours.
5. If a neighbour's indegree becomes 0, add it to the queue.
6. Repeat until the queue becomes empty.

Time Complexity:
    O(V + E)

Space Complexity:
    O(V)

where,
V = number of vertices
E = number of edges

Note:
• Kahn's Algorithm uses BFS.
• It works only for Directed Acyclic Graphs (DAGs).
• If fewer than V vertices are processed, the graph contains
  a cycle and topological sorting is not possible.
"""

from collections import deque as dq

def topologicalSort(adj, indeg):
    indeg = indeg.copy() # to preserve the original indegree of vertices
    q = dq()
    
    for vertex in range(len(indeg)):
        if indeg[vertex] == 0:
            q.append(vertex)

    res = []
    
    while q:
        curr = q.popleft()
        res.append(curr)
    
        for neighbour in adj[curr]:
            indeg[neighbour] -= 1
            if indeg[neighbour] == 0:
                q.append(neighbour)

    if len(res) != len(adj):
        return None # cycle exists

    return res