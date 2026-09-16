"""
N-Queens

Problem:
    Given an integer n, place n queens on an n × n chessboard such that
    no two queens attack each other.

    A queen can attack another queen if they share:

        • Same row
        • Same column
        • Same diagonal

Backtracking Pattern:
    We place exactly one queen in each column.

    At every column:
        1. Try every row as a possible position.
        2. Check whether placing a queen there is safe.
        3. If safe, place the queen.
        4. Explore the next column.
        5. Remove the queen and try another row.

Why one queen per column?
    Since we place exactly one queen in every column, column conflicts
    are automatically avoided.

    Therefore, `isSafe()` only needs to check:
        • Left side of the current row
        • Upper-left diagonal
        • Lower-left diagonal

Base Case:
    When `col == n`, all n columns have successfully received a queen,
    so we have found one valid board configuration.

Time Complexity:
    O(N!)

    At each column, we try multiple rows, but row/diagonal constraints
    significantly reduce the search space.

Space Complexity:
    O(N²)

    The board requires O(N²) space.
    The recursion depth is O(N).

where,
N = size of the chessboard

Note:
• Exactly one queen is placed in each column.
• The board is modified in-place during backtracking.
• A copy of the board is stored whenever a valid solution is found.
"""

def isSafe(row, col, n, board): # to check validity of the cell
    for c in range(col): # to check the left side
        if board[row][c]:
            return False

    r, c = row - 1, col - 1
    while r >= 0 and c >= 0: # to check the upper-left side
        if board[r][c]:
            return False

        r -= 1
        c -= 1

    r, c = row + 1, col - 1
    while r < n and c >= 0: # to check the lower-left side
        if board[r][c]:
            return False

        r += 1
        c -= 1

    return True

def nQueens(n):
    rows, cols = n,  n
    board = [[False] * cols for _ in range(rows)]
    result = []

    def backtrack(col):
        nonlocal board

        if col == n: # base case: all columns till now must have been processed
            result.append([row.copy() for row in board])
            return

        for row in range(n):
            if not isSafe(row, col, n, board): # constraint: to to check whether the cell is safe to place the queen or not
                continue

            board[row][col] = True # choose
            backtrack(col + 1) # explore
            board[row][col] = False # undo

    backtrack(0)

    return result