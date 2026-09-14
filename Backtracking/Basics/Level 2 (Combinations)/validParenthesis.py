"""
Generate Valid Parentheses

Problem:
    Given n pairs of parentheses, generate all combinations of
    parentheses that are well-formed/valid.

Backtracking Idea:
    At every step, we have at most two choices:

        1. Add '(' if we have not used all n opening parentheses.
        2. Add ')' only if there are currently unmatched '('.

    The second condition is what guarantees that we never create
    an invalid prefix such as:

        ")"
        "())"

Constraints:
    • open_count <= n
    • close_count <= open_count

Time Complexity:
    O(C(2N, N) * N)

    There are C(2N, N) valid parenthesis combinations, and
    copying each completed string costs O(N).

Space Complexity:
    O(N)

    The recursion depth and current string require O(N)
    auxiliary space, excluding the output.
"""

def isValid(n):
    result = []
    curr = []
    open, close = 0, 0

    def backtrack():
        nonlocal open, close

        # Constraint
        if len(curr) == n * 2: # base case
            result.append("".join(curr))
            return

        # Choice 1
        if open < n:
            curr.append('(') # choose
            open += 1
            backtrack() # explore
            curr.pop() # undo
            open -= 1

        # Choice 2
        if close < open: # Add ')' only when there is an unmatched '('.
            curr.append(')') # choose
            close += 1
            backtrack() # explore
            curr.pop() # undo
            close -= 1

    backtrack()

    return result