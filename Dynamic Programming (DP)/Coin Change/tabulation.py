"""
Coin Change using Tabulation
"""

def countWays(coins, n, s):
    dp = [[0] * (n + 1) for _ in range(s + 1)]

    for i in range(s + 1)