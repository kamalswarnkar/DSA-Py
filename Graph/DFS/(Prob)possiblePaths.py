"""
Possible Paths Between 2 Vertices

Problem:
    Given a Directed Acyclic Graph (DAG) with n nodes labeled
    from 0 to n - 1, count the number of ways to reach vertex d
    from vertex s.

    There is a directed edge from edges[i][0] to edges[i][1].

Idea:
    Perform DFS from s.

    Whenever `dest` is reached, return 1 because one complete
    path from s to d has been found.

    Sum the counts returned by all neighbouring vertices.

Time Complexity:
    O(V + E) per path exploration in the worst case.

Space Complexity:
    O(V)

where,
V = number of vertices
E = number of edges

Note:
• The graph is a DAG, so DFS cannot encounter a cycle.
• No visited array is required because there are no cycles.
"""

def dfs(adj, src, dest):
    if src == dest:
        return 1

    count = 0

    for neighbour in adj[src]:
        count += dfs(adj, neighbour, dest)

    return count

def possiblePaths(edges, n, s, d):
    adj = [[] for _ in range(n)]

    for e in edges:
        u, v = e
        adj[u].append(v)

    count = dfs(adj, s, d)

    return count