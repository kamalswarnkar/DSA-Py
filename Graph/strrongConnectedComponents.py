"""
Finding Strongly Connected Components (SCCs) in a Directed Graph
using Kosaraju's Algorithm (DFS based)


Strongly Connected Component:
    A maximal set of vertices in a directed graph such that
    every vertex is reachable from every other vertex.


Idea:
1. Perform DFS on the original graph and store vertices in a
   stack according to their finishing order.
2. Create the transpose (reversed) graph by reversing every edge.
3. Process vertices in decreasing order of their finishing time.
4. Perform DFS on the transpose graph.
5. Every DFS traversal in the second pass gives one
   Strongly Connected Component.


Time Complexity:
    O(V + E)


Space Complexity:
    O(V + E)


where,
V = number of vertices
E = number of edges


Note:
• Kosaraju's Algorithm uses two DFS traversals.
• The transpose graph contains every original edge reversed.
• The number of DFS traversals in the second pass equals
  the number of Strongly Connected Components.
"""

def dfs_1(adj, src, visited, stack):
    visited[src] = True

    for neighbour in adj[src]:
        if not visited[neighbour]:
            dfs_1(adj, neighbour, visited, stack)

    stack.append(src) # storing according to the finish time

def dfs_2(adj, src, visited):
    visited[src] = True
    print(src, end=" ") # prints vertices belonging to the current SCC

    for neighbour in adj[src]:
        if not visited[neighbour]:
            dfs_2(adj, neighbour, visited)

def totalStrongComponents(adj):
    n = len(adj)

    visited = [False] * n
    stack = []

    for vertex in range(n):
        if not visited[vertex]:
            dfs_1(adj, vertex, visited, stack)

    transpose = [[] for _ in range(n)]

    for u in range(n):
        for v in adj[u]:
            transpose[v].append(u)

    visited = [False] * n
    count = 0 # counting total no of stronglt connected components

    while stack:
        vertex = stack.pop()

        if not visited[vertex]:
            dfs_2(transpose, vertex, visited)
            count += 1

    return count