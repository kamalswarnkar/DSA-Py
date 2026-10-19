"""
Union by Rank in Disjoint Set (DSU)

Problem:
    Implement Disjoint Set Union operations using rank to
    keep the representative trees relatively balanced.

Approach:
    1. Initialize each element as its own parent with rank 0.
    2. Find the representative of each element's set.
    3. During Union, attach the root with smaller rank to the
       root with larger rank.
    4. If both roots have equal rank, attach one root to the
       other and increment the new root's rank.

Time Complexity:
    Find:  O(N) worst case without path compression.
    Union: O(N) worst case without path compression.

Space Complexity: O(N) for the parent and rank arrays.
"""

def disjointSet(n):
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    def find(x):
        if parent[x] == x:
            return x

        return find(parent[x])

    def union(x, y):
        x_rep = find(x)
        y_rep = find(y)

        if x_rep == y_rep:
            return

        if rank[x_rep] > rank[y_rep]:
            parent[y_rep] = x_rep
        elif rank[x_rep] < rank[y_rep]:
            parent[x_rep] = y_rep
        else:
            parent[y_rep] = x_rep
            rank[x_rep] += 1
