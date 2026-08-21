"""
Minimum Steps by Knight


Problem:
    Given a square chessboard of size N × N, the initial position
    and target position of a Knight are given. Find the minimum
    number of steps required for the Knight to reach the target.


Note:
    The given coordinates use 1-based indexing.
    They are converted to 0-based indexing internally.


Idea:
1. Treat every chessboard cell as a graph vertex.
2. From each cell, the Knight can move to at most 8 cells.
3. Perform BFS starting from the source position.
4. Since every Knight move has equal cost (1), BFS guarantees
   the minimum number of moves.
5. Stop when the target position is reached.


Time Complexity:
    O(N²)


Space Complexity:
    O(N²)


where,
N = size of the chessboard


Note:
• BFS is used because every move has the same cost.
• Each cell is visited at most once.
• If the target is unreachable, return -1.
"""

from collections import deque as dq

def bfs(src, des, direc, n):
    visited = [[False] * n for _ in range(n)]

    q = dq([(src[0], src[1], 0)])
    visited[src[0]][src[1]] = True

    while q:
        r, c, steps = q.popleft()

        for dr, dc in direc:
            nr = r + dr
            nc = c + dc

            if (0 <= nr < n) and (0 <= nc < n) and (not visited[nr][nc]):
                if (nr, nc) == des:
                    return steps + 1

                visited[nr][nc] = True
                q.append((nr, nc, steps + 1))

    return -1

def minSteps(knightPos, targetPos, n):
    if knightPos == targetPos:
        return 0
    
    src = (knightPos[0] - 1, knightPos[1] - 1) # converting into 0-based indexing
    des = (targetPos[0] - 1, targetPos[1] - 1)

    direction = [ # all the next possible positions wrt to the current position of knight
        (-2, 1), (-1, 2), 
        (1, 2), (2, 1),
		(-2, -1), (-1, -2), 
        (1, -2), (2, -1)
    ]

    moves = bfs(src, des, direction, n)

    return moves
