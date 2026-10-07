"""
Sum of All Substrings of a Number using Dynamic Programming

Problem:
    Given a number represented as a string, find the sum of
    all possible numeric substrings.

    Example:
        s = "123"

        Substrings:
            1, 2, 3, 12, 23, 123

        Sum:
            1 + 2 + 3 + 12 + 23 + 123 = 164

Approach:
    Dynamic Programming / Mathematical Recurrence

    `dp[i]` represents the sum of all substrings ending at
    index `i`.

    For the current digit `digit[i]`:

        dp[i] = dp[i - 1] * 10 + digit[i] * (i + 1)

    Why?

        Every substring ending at index i - 1 can be extended
        by the current digit.

        For example:

            "123"

        Substrings ending at index 1:
            2
            12

        Extend them with 3:

            23
            123

        Their contribution becomes:

            (2 + 12) * 10 + 3 * 2

        Additionally, the current digit itself forms a new
        substring:

            3

        Therefore, the current digit appears in (i + 1)
        substrings ending at index i.

    We only need the previous DP value, so the complete DP
    table is unnecessary. `prev` stores the previous value.

Time Complexity:
    O(N)

    Each digit is processed exactly once.

Space Complexity:
    O(1)

    Only a constant number of variables are used.

where,
    N = length of the number string
"""

def sumSubstrings(s):
    prev = 0
    total = 0

    for i, ch in enumerate(s):
        digit = int(ch)

        prev = prev * 10 + digit * (i + 1)
        total += prev

    return total