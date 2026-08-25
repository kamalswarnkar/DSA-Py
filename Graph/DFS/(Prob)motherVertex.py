"""
Mother Vertex

Problem:
    Given a directed graph with V vertices labeled from 0 to V-1
    and a list of directed edges, find a Mother Vertex.

A Mother Vertex is a vertex from which all other vertices
can be reached.

If multiple Mother Vertices exist, return the smallest one.
If no Mother Vertex exists, return -1.

---------------------------------------------------------------
Approach I: Try every vertex
---------------------------------------------------------------

For every vertex:
    1. Perform DFS.
    2. Count the number of reachable vertices.
    3. If all V vertices are reached, the vertex is a Mother Vertex.

Time Complexity:
    O(V × (V + E))

Space Complexity:
    O(V)

---------------------------------------------------------------
Approach II: Optimized
---------------------------------------------------------------

Idea:
1. Perform DFS for every unvisited vertex.
2. Store the last vertex from which a new DFS starts.
3. This vertex is the only possible Mother Vertex candidate.
4. Perform one final DFS from the candidate.
5. If all vertices are visited, the candidate is a Mother Vertex.
   Otherwise, no Mother Vertex exists.

Time Complexity:
    O(V + E)

Space Complexity:
    O(V)

Note:
• The final DFS verification is necessary.
• Since vertices are processed from 0 to V-1, the optimized
  approach also returns the smallest Mother Vertex when multiple
  Mother Vertices exist.
"""

# ---------------------------------------------------------------
# Approach I - Not Optimized
# ---------------------------------------------------------------
def dfsRec_I(adj, src, visited):
    visited[src] = True
    count = 1

    for neighbour in adj[src]:
        if not visited[neighbour]:
            count += dfsRec_I(adj, neighbour, visited)

    return count

def motherVertex_I(V, edges):
    adj = [[] for _ in range(V)]

    for e in edges:
        adj[e[0]].append(e[1])

    for vertex in range(V):
        visited = [False] * V

        count = dfsRec_I(adj, vertex, visited)

        if count == V:
            return vertex

    return -1

# ---------------------------------------------------------------
# Approach II - Optimized
# ---------------------------------------------------------------
def dfsRec_II(adj, src, visited):
    visited[src] = True

    for neighbour in adj[src]:
        if not visited[neighbour]:
            dfsRec_II(adj, neighbour, visited)


def motherVertex_II(V, edges):
    adj = [[] for _ in range(V)]

    visited = [False] * V

    for e in edges:
        adj[e[0]].append(e[1])

    mother_vertex = -1

    # Find the only possible Mother Vertex candidate.
    for vertex in range(V):
        if not visited[vertex]:
            dfsRec_II(adj, vertex, visited)
            mother_vertex = vertex

    # Verify the candidate.
    visited = [False] * V
    dfsRec_II(adj, mother_vertex, visited)

    if all(visited):
        return mother_vertex
    
    return -1