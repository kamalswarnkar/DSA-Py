"""
Fractional Knapsack

Given items with a weight and value, maximize the total value
that can be placed in a knapsack of capacity `cap`.

Unlike 0/1 Knapsack, fractions of an item can be taken.

Greedy Strategy:
    Always choose the item with the highest value-to-weight ratio
    first.

Idea:
1. Calculate the value/weight ratio for every item.
2. Sort items in decreasing order of this ratio.
3. Take the complete item if it fits.
4. Otherwise, take the fraction that fits and stop.

Time Complexity:
    O(N log N)

Space Complexity:
    O(1) auxiliary space
    (ignoring the sorting implementation)

where,
N = number of items

Note:
• Items are represented as [weight, value].
• Item weights must be greater than 0.
• The input array is sorted in-place.
• Greedy works here because fractions of items are allowed.
"""

def fractionalKnapsack(arr, cap):
    n = len(arr)

    arr.sort(key = lambda x : x[1] / x[0], reverse = True)

    res = 0
    curr_cap = cap

    for weight, value in arr:
        if weight <= curr_cap:
            curr_cap -= weight
            res += value
        else:
            res += (value * curr_cap / weight)
            break

    return res
    