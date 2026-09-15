"""
Word Search

Problem:
    Given an m × n grid of characters and a word, determine whether
    the word exists in the grid.

    The word can be constructed from letters of sequentially adjacent
    cells.

    You may move:

        • Up
        • Down
        • Left
        • Right

    A cell cannot be used more than once in the same word path.

Backtracking Pattern:
    At every step:

        1. Choose the current cell.
        2. Mark it as visited.
        3. Explore all four possible directions.
        4. Undo the choice if no direction leads to a solution.

Time Complexity:
    O(M × N × 3^L)

    We can start from any of the M × N cells.
    After choosing the first cell, there are at most 3 choices
    at each step because we cannot immediately reuse the previous cell.

    L = length of the word.

Space Complexity:
    O(L)

    The recursion depth and visited set can contain at most L cells.

where,
M = number of rows
N = number of columns
L = length of the word
"""

def wordSearch(board, word):
    rows, cols = len(board), len(board[0])

    if not word:
        return False

    if len(word) > rows * cols:
        return False
    
    direction = [
        (0, 1), (-1, 0), (1, 0), (0, -1)
    ]

    visited = set()

    def backtrack(r, c, idx):
        if idx == len(word) - 1: # base case
            return True

        visited.add((r, c)) # choose

        for dr, dc in direction:
            nr = r + dr
            nc = c + dc

            if not (0 <= nr < rows and 0 <= nc < cols): # constraint 1: cell should be within grid
                continue

            if (nr, nc) in visited: # constraint 2: cell should be unvisited
                continue

            if board[nr][nc] != word[idx + 1]: # constraint 3: next char should be correct as per given word
                continue

            if backtrack(nr, nc, idx + 1): # explore
                return True

        visited.remove((r, c)) # undo

        return False

    for row in range(rows):
        for col in range(cols):
            if board[row][col] != word[0]:
                continue

            if backtrack(row, col, 0): # should backtrack from all the matching 1st char of the given word
                return True

    return False