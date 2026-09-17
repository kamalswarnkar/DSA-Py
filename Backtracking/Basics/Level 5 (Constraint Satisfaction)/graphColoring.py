"""
Graph Coloring

Problem:
    Given an undirected graph with V vertices and an integer m,
    determine whether the graph can be colored using at most m
    colors such that no two adjacent vertices have the same color.

    Return True if such a coloring exists, otherwise return False.

Approach:
    Backtracking

Backtracking Idea:
    For each vertex:
        1. Try every available color.
        2. Check whether the color is safe.
        3. If safe, assign the color and move to the next vertex.
        4. If the choice does not lead to a solution, remove the
           color and try another one.

Why Backtracking?
    Choosing a color for one vertex can affect the choices available
    for neighboring vertices. If a choice eventually makes coloring
    impossible, we undo that choice and try another color.

Time Complexity:
    O(M^V)

    For each of V vertices, we can try at most M colors.

Space Complexity:
    O(V)

    O(V) for the coloring array and O(V) recursion depth.

where,
V = number of vertices
M = maximum number of available colors

Note:
• Vertices are processed from 0 to V - 1.
• Colors are represented using integers 0 to M - 1.
• The graph is represented using an adjacency list.
"""


def isSafe(graph, coloring, color, idx):
    for neighbour in graph[idx]: # checking for all the adjacent vertices
        if coloring[neighbour] == color:
            return False

    return True

def graphColoring(graph, m):
    v = len(graph)
    coloring = [-1] * v

    def backtrack(idx):
        if idx == v: # base case: assigned colors to all the vertices
            return True

        for color in range(m): # using upto 'm' colors only
            if isSafe(graph, coloring, color, idx): # Constraint: to check whether the selected color is safe to apply on the vertex
                coloring[idx] = color # choose
                if backtrack(idx + 1): # explore
                    return True
                coloring[idx] = -1 # undo

        return False

    return backtrack(0)