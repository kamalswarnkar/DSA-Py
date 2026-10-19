"""
Find and Union Operations on Disjoint Set (DSU)

Problem:
    Implement Find and Union operations to manage disjoint sets.
    Each element initially belongs to its own set.

Approach:
    1. Initialize each element as its own parent.
    2. Use Find to recursively locate the representative of a set.
    3. Use Union to connect two sets by making one representative
       point to the other, if they belong to different sets.

Time Complexity:
    Find:  O(N) worst case.
    Union: O(N) worst case, due to the Find operations.

Space Complexity: O(N) for the parent array, with O(N) worst-case
                  recursion stack for Find.
"""

def disjointSet(n):
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] == x:
            return x

        return find(parent[x])

    def union(x, y):
        x_rep = find(x)
        y_rep = find(y)

        if x_rep == y_rep:
            return

        parent[y_rep] = x_rep