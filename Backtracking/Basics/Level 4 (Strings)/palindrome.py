"""
Palindrome Partitioning

Problem:
    Given a string, partition it into one or more substrings such that
    every substring in the partition is a palindrome.

    Return all possible palindrome partitions.

Backtracking Pattern:
    At every position, choose where the current substring should end.

    For each possible ending position:
        1. Choose a substring.
        2. Check whether it is a palindrome.
        3. If valid, explore the remaining string.
        4. Undo the choice and try the next partition.

Key Idea:
    `start_idx` represents the beginning of the next substring.

    If s = "aab", possible choices from index 0 are:
        "a"  → valid → explore "ab"
        "aa" → valid → explore "b"
        "aab" → invalid → skip

Time Complexity:
    O(N * 2^N)

    There can be O(2^(N-1)) possible partitions.
    Checking whether a substring is a palindrome can take O(N),
    so the overall worst-case complexity is O(N * 2^N).

Space Complexity:
    O(N)

    O(N) recursion depth and O(N) space for the current partition,
    excluding the space required to store the final result.

where,
N = length of the string

Note:
• Every substring in the final partition must be a palindrome.
• The original order of characters is always preserved.
• `start_idx` ensures that no character is skipped or reused.
"""

def isPalindrome(s): # to validate the choice
    n = len(s)
    i, j = 0, n - 1

    while i < j:
        if s[i] != s[j]:
            return False

        i += 1
        j -= 1

    return True

def partition(s):
    n = len(s)
    result = []
    curr = []

    def backtrack(start_idx):
        # The entire string has been partitioned successfully
        if start_idx == n: # base case
            result.append(curr.copy())
            return

        for end in range(start_idx, n):
            substring = s[start_idx : end + 1]

            if not isPalindrome(substring): # main constraint
                continue

            curr.append(substring) # choose
            backtrack(end + 1) # explore
            curr.pop() # undo

    backtrack(0)

    return result