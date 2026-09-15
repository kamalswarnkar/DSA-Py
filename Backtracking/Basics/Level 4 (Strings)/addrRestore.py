"""
Restore IP Addresses

Problem:
    Given a string containing only digits, return all possible valid
    IP addresses that can be formed by inserting exactly three dots.

    A valid IP address contains exactly four parts.

    Each part:
        • Must be between 0 and 255.
        • Cannot contain leading zeros unless the part is exactly "0".

Backtracking Pattern:
    At every position, choose a part containing 1 to 3 digits.

        1. Choose a possible IP part.
        2. Validate the part.
        3. Explore the remaining digits.
        4. Undo the chosen part.

    We need exactly 4 parts to form an IP address.

Time Complexity:
    O(3^N)

    At every position, we can try at most 3 possible part lengths.
    In practice, the recursion is heavily constrained because an IP
    address can contain only 4 parts, each having at most 3 digits.

Space Complexity:
    O(N)

    The recursion depth is at most 4 and the current partition can
    contain at most 4 parts. The output space is excluded.

where,
N = length of the input string

Note:
• Exactly 4 parts must be created.
• Each part can contain at most 3 digits.
• "0" is valid, but "00", "01", etc. are invalid.
• The input string itself is not modified.
"""

def validAddr(ipaddr):
    n = len(ipaddr)
    result = []
    curr = []
    count = 0

    def backtrack(st_idx):
        nonlocal count

        if count == 4: # base case
            if st_idx == n:
                result.append(".".join(curr))
            return

        for end in range(st_idx, min(st_idx + 3, n)):
            part = ipaddr[st_idx:end + 1] 

            if len(part) > 1 and part[0] == '0': # constraint 1: no leading zero unless the part is exactly "0"
                continue

            if int(part) > 255: # constraint 2: Part must be between 0 and 255
                continue

            curr.append(part) # choose
            count += 1
            backtrack(end + 1) # explore
            curr.pop() # pop
            count -= 1

    backtrack(0)

    return result