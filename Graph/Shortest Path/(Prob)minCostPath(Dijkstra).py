"""
Minimum Cost Path

Problem:
    Given a square grid of size N, each cell contains an integer
    cost representing the cost of traversing that cell.

    Find the minimum cost path from the top-left cell to the
    bottom-right cell.

    From cell (i, j), movement is allowed to:
        (i, j - 1)
        (i, j + 1)
        (i - 1, j)
        (i + 1, j)

Using Dijkstra's Algorithm

Idea:
    Treat every cell as a vertex of a graph.

    Moving from one cell to an adjacent cell represents an edge,
    whose cost is the cost of entering the destination cell.

    Since all cell costs are non-negative, Dijkstra's Algorithm
    can be used.

Time Complexity:
    O(N² log N)

Space Complexity:
    O(N²)

where,
N = size of the grid

Note:
• The cost of the starting cell is included.
• The first time the destination is removed from the min-heap,
  its minimum cost has been finalized.
"""

from heapq import heappush, heappop

def minCostPath(adjM):
    V = len(adjM)

    dist = [[float("inf")] * V for _ in range(V)]
    dist[0][0] = adjM[0][0] # Starting cell's cost is included.

    direction = [
        (0, -1), (0, 1),
        (-1, 0), (1, 0)
    ]

    q = [(adjM[0][0], 0, 0)]

    while q:
        cost, r, c = heappop(q)

        if (r, c) == (V - 1, V - 1):
            return cost

        if cost > dist[r][c]: # Ignore stale heap entries.
            continue

        for dr, dc in direction:
            nr = r + dr
            nc = c + dc

            if (0 <= nr < V) and (0 <= nc < V):
                new_cost = cost + adjM[nr][nc]

                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heappush(q, (new_cost, nr, nc))

    return -1