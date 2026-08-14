"""
Topological Sort using DFS

Topological Sort is a linear ordering of the vertices of a
Directed Acyclic Graph (DAG) such that for every directed edge
u → v, vertex u appears before vertex v.

Idea:
1. Perform DFS from every unvisited vertex.
2. Recursively visit all unvisited neighbours.
3. After all neighbours of a vertex are processed, push the
   vertex onto a stack.
4. Pop the stack to obtain the topological ordering.

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
"""


def dfs(adj, src, stack, visited):
    visited[src] = True

    for neighbour in adj[src]:
        if not visited[neighbour]:
            dfs(adj, neighbour, stack, visited)

    stack.append(src)

def topologicalSort(adj):
    st = []
    visited = [False] * len(adj)

    for vertex in range(len(adj)):
        if not visited[vertex]:
            dfs(adj, vertex, st, visited)

    while st:
        curr = st.pop()
        print(curr, end=" ")