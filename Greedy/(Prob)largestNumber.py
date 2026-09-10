"""
Largest N-Digit Number with Given Digit Sum

Problem:
    Given two integers n and s, find the largest possible number
    that can be formed using exactly n digits such that the sum
    of all digits equals s.

    If it is not possible to construct such a number, return "-1".
    Return the result as a string.

Greedy Strategy:
1. At every position, place the largest possible digit.
2. The maximum digit we can place is 9.
3. Therefore, take min(9, remaining_sum).
4. Continue until all n positions are filled.

Why does this work?
    Since we want the largest number, the leftmost digit has
    the highest place value. Therefore, we should maximize it
    before considering the next digit.

Feasibility:
    The maximum sum possible with n digits is 9 × n.
    Therefore, if s > 9 × n, constructing the number is impossible.

Time Complexity:
    O(N)

Space Complexity:
    O(N)

where,
N = number of digits

Note:
• Each digit can be from 0 to 9.
• Leading zero is allowed only when the problem permits a
  number such as 000...0; the returned result still has n digits.
• The input sum must satisfy 0 <= s <= 9 × n.
"""

def largestNumber(n, s):
    if s > 9*n:
        return -1

    res = []
    rem = s

    for _ in range(n):
        dgt = min(9, rem)
        res.append(str(dgt))
        rem -= dgt

    return "".join(res)
