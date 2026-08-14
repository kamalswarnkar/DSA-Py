"""
Shortest Path in a DAG (Directed Acyclic Graph)

Find the shortest distance from a given source vertex to
every other vertex in a weighted DAG.

Idea:
1. Find the topological ordering of the DAG using Kahn's Algorithm.
2. Initialize the source distance as 0 and all other distances as INF.
3. Process vertices in topological order.
4. For every outgoing edge, relax the edge:
       dist[v] = min(dist[v], dist[u] + weight[u][v])
5. Since every vertex is processed only after all its incoming
   dependencies, all required shortest distances are already
   finalized when the vertex is processed.

Time Complexity:
    O(V + E)

Space Complexity:
    O(V)

where,
V = number of vertices
E = number of edges

Note:
• This algorithm works for weighted DAGs.
• Edge weights can be positive, zero, or negative.
• A DAG cannot contain a cycle.
• Topological sorting is used to determine the order in which
  vertices should be relaxed.
"""

from collections import deque as dq

INF = float("inf")

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

def shortestPath(adj, src, indeg, weight): # it is a weighted graph, 'weight' is the matrix containing weight of every edge
    dist = [INF] * len(adj)
    dist[src] = 0

    topo_sort = topologicalSort(adj, indeg)

    if not topo_sort:
        return None # graph is not a DAG

    for vertex in topo_sort:
        if dist[vertex] == INF:
            continue
        
        for neighbour in adj[vertex]:
            new_dist = dist[vertex] + weight[vertex][neighbour]

            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist

    return dist
    
