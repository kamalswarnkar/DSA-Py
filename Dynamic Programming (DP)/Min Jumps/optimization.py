"""
Minimum Jumps to Reach the End using Greedy Approach

Problem:
    Given an array `arr` where arr[i] represents the maximum
    number of positions that can be jumped from index i,
    find the minimum number of jumps required to reach the
    last index.

    Return -1 if the last index cannot be reached.

Approach:
    Greedy

    We maintain three variables:

        jumps:
            Number of jumps taken so far.

        curr_end:
            Farthest index reachable using the current number
            of jumps.

        farthest:
            Farthest index reachable from any position within
            the current jump range.

    While traversing the current range, we continuously update
    `farthest`.

    When we reach `curr_end`, the current jump is exhausted.
    We must make another jump, so we extend the range to
    `farthest`.

    This greedy choice is optimal because instead of choosing
    one specific next index, we consider the entire range that
    can be reached and always extend it as far as possible.

Time Complexity:
    O(N)

    The array is traversed only once.

Space Complexity:
    O(1)

    Only a constant number of variables are used.

where,
    N = length of the array
"""

def minJumps(arr):
    n = len(arr)

    if n <= 1:
        return 0

    jumps, farthest, curr_end = 0, 0, 0

    for i in range(n - 1):
        farthest = max(farthest, arr[i] + i) # Farthest position reachable from the current range.

        if i == curr_end: # We have reached the end of the current jump range.
            if farthest == curr_end: # If we cannot move any further, destination is unreachable.
                return -1

            jumps += 1
            curr_end = farthest

            if curr_end >= n - 1: # We can already reach the destination.
                return jumps

    return -1