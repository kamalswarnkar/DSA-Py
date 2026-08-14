"""
Topological Sort using DFS

Topological Sort is a linear ordering of the vertices of a
Directed Acyclic Graph (DAG) such that for every directed edge
u → v, vertex u appears before vertex v.

Idea:
1. Maintain two arrays:
   • visited -> tracks whether a vertex has been visited.
   • recSt   -> tracks whether a vertex is in the current DFS path.
2. Perform DFS from every unvisited vertex.
3. Recursively visit all unvisited neighbours.
4. If a neighbour is already present in recSt, a cycle exists.
5. After all neighbours are processed:
   • Remove the vertex from recSt.
   • Push the vertex onto the stack.
6. Pop the stack to obtain the topological ordering.

Time Complexity:
    O(V + E)

Space Complexity:
    O(V)

where,
V = number of vertices
E = number of edges

Note:
• This is the DFS-based approach to Topological Sorting.
• The vertex is added to the stack only after all its
  neighbours have been processed.
• The final ordering is obtained by reversing the
  DFS finishing order.
• Topological sorting is possible only for a DAG.
• recSt is used to detect cycles in the directed graph.
"""


def dfs(adj, src, stack, visited, recSt):
    visited[src] = True
    recSt[src] = True

    for neighbour in adj[src]:
        if not visited[neighbour]:
            if dfs(adj, neighbour, stack, visited, recSt):
                return True

        elif recSt[neighbour]:
            return True

    recSt[src] = False
    stack.append(src)

    return False

def topologicalSort(adj):
    st = []
    visited = [False] * len(adj)
    recSt = [False] * len(adj)

    for vertex in range(len(adj)):
        if not visited[vertex]:
            if dfs(adj, vertex, st, visited, recSt):
                return None # cycle exists

    res = []

    while st:
        res.append(st.pop())

    return res