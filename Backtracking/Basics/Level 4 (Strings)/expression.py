"""
Expression Generation

Problem:
    Given a string containing digits and a target integer, insert the
    operators:

        +
        -
        *

    between digits to form expressions whose evaluated result equals
    the target.

    You may not reorder the digits.

    Numbers with leading zeros are not allowed unless the number itself
    is 0.

Backtracking Pattern:
    At every position, choose how many digits will form the next number.

    For the chosen number:
        1. Choose the number.
        2. Try '+', '-', and '*'.
        3. Explore the remaining digits.
        4. Backtrack and try another choice.

State:
    idx             -> current position in the digit string
    value           -> evaluated value of the expression so far
    prev             -> previous operand, needed to handle multiplication
    expression      -> current expression being constructed

Example:
    Expression: 2 + 3 * 4

    When processing *4:

        current_value = 5
        previous_value = 3

    We first remove the previous `3`:

        5 - 3 = 2

    Then replace it with:

        3 * 4 = 12

    Therefore:

        2 + 12 = 14


Time Complexity:
    O(N * 4^N)

    At each position, we can choose different number lengths and
    operators. The expression-building process can generate
    exponentially many possibilities.

Space Complexity:
    O(N)

    The recursion depth and expression under construction require
    O(N) auxiliary space, excluding the output.

where,
N = length of the digit string

Note:
• Digits cannot be reordered.
• A number cannot contain leading zeros.
• Multiplication requires special handling because of operator precedence.
"""

def expression(digits, target):
    n = len(digits)
    result = []

    def backtrack(idx, val, prev, expr):
        if idx == n: # base case
            if val == target:
                result.append(expr)
            return

        for end in range(idx, n):
            if end > idx and digits[idx] == '0': # constraint : no leading zeros
                continue

            num_str = digits[idx: end + 1]
            num = int(num_str)

            if idx == 0: # 1st number - no operator before
                backtrack(end + 1, num, num, num_str)
            else:
                backtrack(end + 1, val + num, num, expr + '+' + num_str) # addition
                backtrack(end + 1, val - num, -num, expr + '-' + num_str) # substraction
                # multiplication
                new_val = val - prev + (prev * num)
                backtrack(end + 1, new_val, prev*num, expr + '*' + num_str)

    backtrack(0, 0, 0, "")

    return result