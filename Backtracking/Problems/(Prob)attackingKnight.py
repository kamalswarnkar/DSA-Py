"""
Non-Attacking Black and White Knights

Problem:
    Given an n x m chessboard, place one black knight and one white
    knight such that:

        • They occupy different squares.
        • They do not attack each other.

A knight attacks another knight if their row and column differences
are:

    |dr| = 1 and |dc| = 2
    OR
    |dr| = 2 and |dc| = 1

The black and white knights are distinct, so placing:
    Black at A, White at B

is different from:
    Black at B, White at A.


METHOD 1: Backtracking
----------------------
Try every possible position for the black knight and then every
possible non-attacking position for the white knight.

Time Complexity:
    O((N * M)²)

Space Complexity:
    O(1) auxiliary space
    O(N * M) recursion depth in the general backtracking structure,
    although this particular recursion has depth only 2.


METHOD 2: Combinatorial Optimization
-------------------------------------
Instead of checking every pair of positions:

    1. Count all possible ordered placements.
    2. Subtract the placements where the knights attack each other.

Total ordered placements:

    (N * M) * (N * M - 1)

Two knights attack only when they occupy opposite corners of a
2 x 3 or 3 x 2 rectangle.

Time Complexity:
    O(1)

Space Complexity:
    O(1)
"""

# Method 1: Backtracking - O((n*m)^2)
def isAttacking(r1, r2, c1, c2):
    """
    Possible attacking positions in one move:
    (-2, -1), (-2,  1),
    ( 2, -1), ( 2,  1),
    (-1, -2), (-1,  2),
    ( 1, -2), ( 1,  2)
    """
    dr = abs(r1 - r2)
    dc = abs(c1 - c2)

    return (dr == 1 and dc == 2) or (dr == 2 and dc == 1)

def backtrack(n, m, black_r, black_c, placed):
    if placed == 2: # if both knights are already placed
        return 1

    count = 0

    for r in range(n):
        for c in range(m):
            if placed == 0: # to place black knight first
                count += backtrack(n, m, r, c, 1)
            else: # if black knight is already placed and now to place white knight in non-attacking position
                if r == black_r and c == black_c: # to avoid placing white knight in the same position as black knight
                    continue
                if isAttacking(black_r, r, black_c, c): # to avoid placing white knight in an attacking position
                    continue

                count += 1

    return count

def numOfWays(n, m):
    return backtrack(n, m, -1, -1, 0) 

# Method 2: Combinatorics - O(1)
def numOfWaysOptimized(n, m):
    """
    Choose black: n*m
    Choose white from remaining squares: n*m - 1
    """
    total_squares = n * m
    total = total_squares * (total_squares - 1)

    """
    Instead of checking every pair, count the number of 2 × 3 and 3 × 2 rectangles.
    A 2 × 3 rectangle has 2 knight attacking pairs.
        Number of such rectangles: (n-1)(m-2)
        Therefore attacking unordered pairs from these: 2(n−1)(m−2)
    
    A 3 × 2 rectangle has 2 knight attacking pairs.
        Number of such rectangles: (n-2)(m-1)
        Therefore attacking unordered pairs from these: 2(n−2)(m−1)
    
    Therefore:
        attacking placements: 4[(n−1)(m−2)+(n−2)(m−1)]
    """

    # to handle boards with size smaller than 2 × 3 or 3 × 2, else either of (n−1), (m−2), (n−2), or (m−1) can become negative
    rectangles_2x3 = max(0, n - 1) * max(0, m - 2)
    rectangles_3x2 = max(0, n - 2) * max(0, m - 1)

    attacking = 4 * (rectangles_2x3 + rectangles_3x2)

    return total - attacking
