"""
Largest Number in K Swaps

Problem:
    Given a number k and a string s of digits representing a
    positive integer, build the largest number possible by
    performing at most k swaps between its digits.

Approach:
    Backtracking + Greedy Choice

Idea:
    1. Process the number from left to right.
    2. Find the largest digit present from the current position
       onwards.
    3. If the current digit is already the largest available digit,
       no swap is needed; move to the next position.
    4. Otherwise, try swapping the current digit with every
       occurrence of the largest available digit.
    5. Recursively solve the remaining positions with k - 1 swaps.
    6. Undo the swap after exploring that choice.
    7. Keep track of the largest number encountered.

Why try only the maximum digit?
    To maximize the number, we should make the earliest possible
    position as large as possible. Therefore, at each position,
    only swaps involving the largest available digit can lead
    to an optimal result.

Time Complexity:
    O(N! / (N-K)!) in the worst case, depending on the number of
    possible swaps explored.

Space Complexity:
    O(N)

where,
N = number of digits
K = maximum number of swaps
"""

def findMaximumNum(s, k):
    s = list(s)
    n = len(s)
        
    ans = [''.join(s)]
        
    def dfs(pos, k):
        nonlocal ans, s
            
        if k == 0 or pos == n:
            ans[0] = max(ans[0], ''.join(s))
            return
            
        max_dgt = max(s[pos:])
            
        if s[pos] == max_dgt:
            dfs(pos + 1, k)
            return
            
        for j in range(pos + 1, n):
            if s[j] == max_dgt:
                s[pos], s[j] = s[j], s[pos]
                    
                dfs(pos + 1, k - 1)
                    
                s[pos], s[j] = s[j], s[pos]
        
    dfs(0, k)
        
    return ans[0]