"""
Letter Combinations of a Phone Number

Problem:
    Given a string containing digits from 2 to 9, return all possible
    letter combinations that the number could represent according to
    the traditional phone keypad.

Mapping:
    2 → abc
    3 → def
    4 → ghi
    5 → jkl
    6 → mno
    7 → pqrs
    8 → tuv
    9 → wxyz

Backtracking Idea:
    For each digit, choose one of its possible letters.

    Example:
        digits = "23"

        For '2' → choose a, b, or c
        For '3' → choose d, e, or f

        This creates:
            ad, ae, af
            bd, be, bf
            cd, ce, cf

Time Complexity:
    O(4^N * N)

    Each digit has at most 4 possible letters, giving up to 4^N
    combinations. Copying each combination costs O(N).

Space Complexity:
    O(N)

    The recursion depth and current combination require O(N)
    auxiliary space, excluding the output.
"""

def letterComb(digits):
    mapping = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz'
    }
    result = []
    curr = []

    def backtrack(idx):
        # Constraint
        if len(curr) == len(digits): # base case
            result.append(''.join(curr))
            return

        # Choice
        for letter in mapping[digits[idx]]:
            curr.append(letter)
            backtrack(idx + 1)
            curr.pop()

    backtrack(0) # Start Index

    return result
