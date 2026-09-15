"""
Next-Level Arrangement Problem

Problem:
    Given n distinct elements, generate all possible permutations
    with the additional constraint that no element remains in its
    original position.

    Such a permutation is called a derangement.

Example:
    arr = [1, 2, 3]

    Valid derangements:
        [2, 3, 1]
        [3, 1, 2]

Backtracking Idea:
    At each position `pos`:

        1. Choose an unused element.
        2. Reject it if it is the element originally present
           at position `pos`.
        3. Place the element and recursively solve the next position.
        4. Undo the choice.

Constraint:
    arr[idx] != arr[pos]

    This guarantees that the element originally at position `pos`
    cannot remain in that position.

Time Complexity:
    O(N * N!)

    In the worst case, we may explore permutations up to N!,
    with O(N) work required to copy each valid permutation.

Space Complexity:
    O(N)

    The recursion depth, current permutation, and `used[]` array
    require O(N) auxiliary space, excluding the output.

where,
N = number of elements
"""

def derangement(arr):
    n = len(arr)
    result = []
    curr = []
    used = [False] * n

    def backtrack(pos):
        if pos == n: # base case
            result.append(curr)
            return

        for idx in range(n):
            if used[idx]: # used
                continue

            if arr[idx] == arr[pos]: # main constraint
                continue

            used[idx] = True

            curr.append(arr[idx]) # choose
            backtrack(pos + 1) # explore
            curr.pop() # undo

            used[idx] = False

    backtrack(0)

    return result