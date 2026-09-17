"""
Rat in a Maze

Problem:
    Given an n × n maze represented by a binary matrix:

        1 → Open cell
        0 → Blocked cell

    A rat starts at the top-left cell (0, 0) and must reach
    the bottom-right cell (n-1, n-1).

    The rat can move in four directions:

        D → Down
        L → Left
        R → Right
        U → Up

    A cell cannot be visited more than once in the same path.

    Return all possible paths from source to destination.

Approach:
    Backtracking

Backtracking Idea:
    1. Start from (0, 0).
    2. Try moving in each of the four possible directions.
    3. Move only if the next cell:
           • is inside the maze,
           • is open,
           • has not been visited in the current path.
    4. Add the movement direction and mark the cell as visited.
    5. Recursively explore from the new cell.
    6. After returning, undo the choice so another path can be tried.

Time Complexity:
    O(4^(N²))

    In the worst case, from each cell we can try up to 4 directions.
    The actual complexity is lower because visited cells prevent cycles.

Space Complexity:
    O(N²)

    The visited set can contain at most N² cells, and the recursion
    depth can also reach O(N²).

where,
N = size of the maze

Note:
• `visited` represents cells visited in the current path only.
• Backtracking removes a cell from `visited` after exploring it,
  allowing that cell to be used in another possible path.
"""

def isSafe(row, col, n, maze, vis):
    if (0 <= row < n) and (0 <= col < n) and maze[row][col] == 1 and (row, col) not in vis:
        return True

    return False

def ratMaze(maze):
    n = len(maze)
    result = []
    curr = []
    direction = {
        (1,  0) : 'D', # down
        (0, -1) : 'L', # left
        (0,  1) : 'R', # right
        (-1, 0) : 'U'  # up
    }
    visited = set()

    def backtrack(row, col):
        if row == n - 1 and col == n - 1: # base case: reached the last cell
            result.append("".join(curr))
            return

        for dr, dc in direction: # check for all 4 directions
            nr = row + dr
            nc = col + dc

            if isSafe(nr, nc, n, maze, visited):
                curr.append(direction[(dr, dc)]) # choose
                visited.add((nr, nc))

                backtrack(nr, nc) # explore

                curr.pop() # undo
                visited.remove((nr, nc))

    visited.add((0, 0)) # source already visited
    backtrack(0, 0)

    return result