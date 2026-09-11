"""
Rat in a Maze

Given an N x N binary maze:
    1 -> Cell can be visited.
    0 -> Cell cannot be visited.

Starting from (0, 0), find a path to (N-1, N-1).

In this implementation, the rat can move only:
    • Down
    • Right

Approach:
    Backtracking

Idea:
    1. Start from the top-left cell.
    2. Mark the current cell as part of the solution.
    3. Try moving Down.
    4. If Down does not lead to a solution, try moving Right.
    5. If neither direction works, remove the current cell
       from the solution and backtrack.

Time Complexity:
    O(2^(N²)) in the worst case.

Space Complexity:
    O(N²)

Note:
    The solution matrix stores the path:
        1 -> Cell belongs to the solution path.
        0 -> Cell does not belong to the solution path.
"""

def printSolution(sol):
    n = len(sol)

    for i in range(n):
        for j in range(n):
            print(sol[i][j], end=" ")
        print()

def isSafe(maze, i, j):
    return i < len(maze) and j < len(maze) and maze[i][j] == 1

def solveMazeRec(maze, i, j, sol):
    if i == len(maze) - 1 and j == len(maze) - 1 and maze[i][j] == 1:
        sol[i][j] = 1
        return True

    if isSafe(maze, i, j):
        sol[i][j] = True

        if solveMazeRec(maze, i + 1, j, sol):
            return True
        if solveMazeRec(maze, i, j + 1, sol):
            return True

        sol[i][j] = 0

    return False

def solveMaze(maze):
    n = len(maze)

    sol = [[0] * n for _ in range(n)]

    if not solveMazeRec(maze, 0, 0, sol):
        print("Solution Doesn't Exist")
        return False

    printSolution(sol)

    return True
