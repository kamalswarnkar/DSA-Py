"""
Check for Path in a 2D Grid with Obstacles

Problem:
    Given an n × n grid containing:
        1 : Source cell
        2 : Destination cell
        3 : Traversable cell
        0 : Wall

    Determine whether a path exists from the source to the
    destination.

    Movement is allowed in four directions:
        Up, Down, Left, Right

Idea:
    Treat every traversable cell as a vertex in a graph and
    perform BFS starting from the source.

    BFS explores all cells reachable from the source. If the
    destination is encountered, a path exists.

Time Complexity:
    O(N²)

Space Complexity:
    O(N²)

where,
N = size of the grid
"""

from collections import deque as dq

def isPathPossible(mat):
    n = len(mat)
    src = (-1, -1)
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                src = (i, j)
                break

    direction = [
                (-1, 0),
        (0, -1),        (0, 1),
                (1, 0)
    ]

    q = dq([(src[0], src[1])])
    visited[src[0]][src[1]] = True

    while q:
        r, c = q.popleft()

        for dr, dc in direction:
            nr = r + dr
            nc = c + dc

            if (0 <= nr < n) and (0 <= nc < n) and (not visited[nr][nc]):
                if mat[nr][nc] == 3:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                elif mat[nr][nc] == 2:
                    return True

    return False