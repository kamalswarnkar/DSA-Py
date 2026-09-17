"""
Sudoku Solver

Problem:
    Given a partially filled N × N Sudoku board, fill the empty cells
    so that:

        • Every row contains numbers 1 to N without repetition.
        • Every column contains numbers 1 to N without repetition.
        • Every sqrt(N) × sqrt(N) sub-grid contains numbers 1 to N
          without repetition.

    Empty cells are represented by ".".

Approach:
    Backtracking

Backtracking Idea:
    1. Process the board cell by cell.
    2. If the current cell is already filled, move to the next cell.
    3. If the cell is empty, try every number from 1 to N.
    4. Place a number only if it is valid in the:
           • current row
           • current column
           • current sub-grid
    5. Recursively solve the remaining cells.
    6. If the choice does not lead to a solution, undo it and try
       another number.

Time Complexity:
    O(N^(N²)) in the worst case.

    There are N² cells and up to N choices for each cell.
    Practical performance is much better because invalid choices
    are pruned by the Sudoku constraints.

Space Complexity:
    O(N²)

    The board itself uses O(N²) space, while recursion uses
    O(N²) stack space in the worst case.

Note:
    • 0 / "." represents an empty cell depending on the input format.
    • This implementation uses "." for empty cells.
    • The board is modified in-place.
    • N must be a perfect square.
"""

import math

def isSafe(num, row, col, n, board):
    for r in range(n): # check the current column
        if board[r][col] == num:
            return False

    for c in range(n): # check the current row
        if board[row][c] == num:
            return False

    grid_size = int(math.sqrt(n)) # find the sixe of sub-grid

    grid_row = row - row % grid_size # starting row
    grid_col = col - col % grid_size # starting column

    # check for the whole subgrid
    for r in range(grid_row, grid_row + grid_size):
        for c in range(grid_col, grid_col + grid_size):
            if board[r][c] == num:
                return False

    return True

def sudoku(board):
    n = len(board)

    def backtrack(row, col):
        if col == n: # base case 1: if current row is finished
            row += 1
            col = 0

        if row == n: # base case 2: if all cells are finished
            return True

        if board[row][col] != '.': # if cell is already filled
            return backtrack(row, col + 1)

        for num in range(1, n + 1):
            if isSafe(str(num), row, col, n, board): # constraint: check if the num is valid for the cell or not
                board[row][col] = str(num) # choose
                if backtrack(row, col + 1): # explore
                    return True
                board[row][col] = '.' # undo

        return False

    backtrack(0, 0)

    return board