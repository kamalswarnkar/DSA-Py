"""
Minimum Swaps to Sort

Problem:
    Given an array arr[] of distinct elements, find the minimum
    number of swaps required to sort the array in strictly
    increasing order.

It is basically a permutation graph problem

Idea:
1. Sort a copy of the array.
2. Map every value to its correct sorted position.
3. This creates a permutation where:
       current index → correct index
4. Find cycles in this permutation.
5. A cycle of length k requires exactly k - 1 swaps.

Time Complexity:
    O(N log N)

Space Complexity:
    O(N)

where,
N = number of elements

Note:
• All elements are distinct.
• For every cycle of length k, minimum swaps = k - 1.
"""

def length(adj, src, visited):
    curr = src
    count = 0

    while not visited[curr]:
        visited[curr] = True
        count += 1
        curr = adj[curr][0]

        if curr == src:
            break

    return count

def minSwap(arr):
    V = len(arr)
    adj = [[] for _ in range(V)]
    visited = [False] * V
    swap = 0

    sorted_arr = sorted(arr)

    position = {value : i for i, value in enumerate(sorted_arr)} # mapping value → sorted index

    for i in range(V):
        adj[i].append(position[arr[i]]) # filling adjacency list

    for vertex in range(V):
        if not visited[vertex]:
            cycle_len = length(adj, vertex, visited)

            if cycle_len > 1:
                swap += cycle_len - 1 # for 'k' length tere will be 'k - 1' swaps

    return swap