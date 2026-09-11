"""
Generate Permutations Without "AB"

Given a string, print all permutations that do not contain
"AB" as a substring.

Approach:
    Backtracking

Idea:
1. Generate the permutation one position at a time.
2. At position `l`, try every remaining character.
3. Before placing a character, check whether placing it at
   position `l` would create the forbidden substring "AB".
4. If safe:
       • Swap the character into position l.
       • Recursively generate the remaining permutation.
       • Swap back to restore the original string (backtracking).

Why only check the previous character?
    At position `l`, all positions before `l` are already fixed.
    The only new adjacent pair created by placing string[i] at
    position `l` is:

        string[l - 1] + string[l]

    Therefore, we only need to check whether this pair becomes "AB".

Time Complexity:
    O(N × N!)

    There can be up to N! permutations, and checking/printing
    each permutation takes O(N).

Space Complexity:
    O(N)

    This includes the recursion stack. The string itself is
    modified in-place.

Note:
• The input characters are assumed to be distinct.
• The forbidden substring is "AB".
• Swapping is used to generate permutations in-place.
"""

def isSafe(string, l, i, r):
    if l != 0 and string[l - 1] == 'A' and string[i] == 'B':
        return False
    if r == l + 1 and string[i] == 'A' and string[l] == 'B':
        return False

    return True

def permute(string, l, r):
    if l == r:
        print(string, sep="", end=" ")
        return
    else:
        for i in range(l, r + 1):
            if isSafe(string, l, i, r):
                string[i], string[l] = string[l], string[i]
                permute(string, l + 1, r)
                string[i], string[l] = string[l], string[i]