"""
Rotten Oranges

Problem:
    Given a matrix mat[][], where each cell in the matrix can have
    values 0, 1 or 2 which have the following meaning:
        0 : Empty cell
        1 : Fresh orange
        2 : Rotten orange

Determine the minimum time required so that all the oranges become
rotten. A rotten orange at index (i, j) can rot other fresh oranges
at indexes (i-1, j), (i+1, j), (i, j-1), (i, j+1) (up, down, left
and right) in one unit of time.

Note:
    If it is impossible to rot every orange, return -1.

Idea:
    This is a Multi-Source BFS problem.

    All initially rotten oranges are inserted into the queue
    simultaneously. Each BFS level represents one unit of time.

Time Complexity:
    O(R × C)

Space Complexity:
    O(R × C)

where,
R = number of rows
C = number of columns
"""

from collections import deque as dq

def orangesRot(mat):
    row, col = len(mat), len(mat[0])

    visited = [[False] * col for _ in range(row)]

    q = dq()
    fresh = 0
    count = 0

    for r in range(row):
        for c in range(col):
            if mat[r][c] == 2:
                q.append((r, c))
                visited[r][c] = True
            elif mat[r][c] == 1: # if oranges are fresh
                fresh += 1

    direction = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]

    while q and fresh:
        for _ in range(len(q)):
            r, c = q.popleft()

            for dr, dc in direction:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < row) and (0 <= nc < col) and (not visited[nr][nc]) and (mat[nr][nc] == 1):
                    mat[nr][nc] = 2
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    fresh -= 1

        count += 1

    if fresh: # if there are still fresh oranges not near any rotten orange
        return -1

    return count