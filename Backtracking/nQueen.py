"""
N-Queens Problem

Place N queens on an N x N chessboard such that no two queens
attack each other.

A queen can attack another queen if they are in the same:
    • Row
    • Column
    • Main diagonal
    • Anti-diagonal

Approach:
    Backtracking

Idea:
    1. Place exactly one queen in each column.
    2. For the current column, try placing a queen in every row.
    3. Before placing, check whether the position is safe.
    4. If safe, place the queen and recursively solve the next column.
    5. If the next columns cannot be solved, remove the queen
       and try another row.

Time Complexity:
    O(N!)

Space Complexity:
    O(N²)

Note:
    Since we place exactly one queen per column, we do not need
    to check the current column separately.
"""

def printBoard(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))

def isSafe(row, col, n, board):
    for prev_col in range(col): # Check whether another queen already exists in the same row.
        if board[row][prev_col]:
            return False
        
    r, c = row - 1, col - 1 # Check the upper-left diagonal.

    while r >= 0 and c >= 0:
        if board[r][c]:
            return False

        r -= 1
        c -= 1

    r, c = row + 1, col - 1 # Check the lower-left diagonal.
    
    while r < n and c >= 0:
        if board[r][c]:
            return False
    
        r += 1
        c -= 1

    return True

def solveRec(col, n, board):
    if col == n: # All columns have been successfully assigned a queen.
        return True

    for row in range(n): # Try placing a queen in every row of the current column.
        if isSafe(row, col, n, board): # Only place the queen if it cannot be attacked.
            board[row][col] = True # Choose: place the queen.

            if solveRec(col + 1, n, board): # Explore: solve the remaining columns.
                return True

            board[row][col] = False # Backtrack: this position did not lead to a solution.

    return False # No row in this column can lead to a valid solution.

def solve(n):
    board = [[False] * n for _ in range(n)] # Initially, no queens are placed on the board.

    if not solveRec(0, n, board): # Try to place queens starting from the first column.
        return False

    printBoard(board) # Print the final board.

    return True
