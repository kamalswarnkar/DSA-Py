"""
Sudoku Solver

Given an N x N Sudoku board, fill all empty cells (represented
by 0) such that:

    • Every row contains numbers 1 to N without repetition.
    • Every column contains numbers 1 to N without repetition.
    • Every sqrt(N) x sqrt(N) sub-grid contains numbers 1 to N
      without repetition.

Approach:
    Backtracking

Idea:
    1. Find an empty cell.
    2. Try every number from 1 to N in that cell.
    3. Check whether the number is valid in its:
           • Row
           • Column
           • Sub-grid
    4. If valid, place the number and recursively solve the rest.
    5. If the choice does not lead to a solution, remove the number
       and try another one.
    6. If no number works, backtrack to the previous cell.

Time Complexity:
    O(N^(N²)) in the worst case.

Space Complexity:
    O(N²)

where,
N = size of the Sudoku board

Note:
• 0 represents an empty cell.
• This implementation modifies the board in-place.
• `N` must be a perfect square for the sub-grid calculation.
"""

import math

def isSafe(board, row, col, num):
    n = len(board)

    for c in range(n): # Check whether the number already exists in the current row.
        if board[row][c] == num:
            return False

    for r in range(n): # Check whether the number already exists in the current column.
        if board[r][col] == num:
            return False

    subgrid_size = int(math.sqrt(n)) # Calculate the size of one Sudoku sub-grid.

    # Find the top-left corner of the sub-grid containing (row, col).
    box_row_start = row - row % subgrid_size
    box_col_start = col - col % subgrid_size

    # Check whether the number already exists in the sub-grid.
    for r in range(box_row_start, box_row_start + subgrid_size):
        for c in range(box_col_start, box_col_start + subgrid_size):
            if board[r][c] == num:
                return False

    return True
 
def solve(board):
    n = len(board)

    # Find the first empty cell.
    row, col = -1, -1 
    isEmpty = True

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                row, col = i, j
                isEmpty = False
                break

        if not isEmpty: # Stop searching once an empty cell has been found.
            break

    if isEmpty: # No empty cells remain, so the Sudoku has been solved.
        return True

    for num in range(1, n + 1):  # Try every possible number in the empty cell.
        if isSafe(board, row, col, num): # Only place the number if it does not violate Sudoku rules.
            board[row][col] = num# Choose: place the number.

            if solve(board): # Explore: recursively solve the remaining board.
                return True

            board[row][col] = 0 # Backtrack: this number did not lead to a valid solution.

    return False # No number can be placed in this cell, so backtrack.