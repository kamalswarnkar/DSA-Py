"""
Longest Chain of Pairs

Problem:
    Given pairs (a, b), find the longest chain such that for every
    consecutive pair:

        (a, b) -> (c, d)

    the condition must satisfy:

        b < c

    A pair can be followed by another pair only if the second
    value of the current pair is smaller than the first value
    of the next pair.

Approach:
    Dynamic Programming

    1. Sort pairs by their first value.
    2. Let dp[i] represent the longest chain ending at pair i.
    3. For every previous pair j:
           if pairs[j][1] < pairs[i][0],
           pair i can be added after pair j.
    4. Take the maximum value in dp.

Time Complexity:
    O(N²)

    Sorting takes O(N log N), and the DP takes O(N²).

Space Complexity:
    O(N)

    For the DP array.

where,
    N = number of pairs
"""

def longestChain(pairs):
    n = len(pairs)

    if n == 0:
        return 0

    pairs.sort(key = lambda x:x[0])

    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if pairs[j][1] < pairs[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)