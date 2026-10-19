"""
Path Compression Optimization in Disjoint Set (DSU)

Problem:
    Optimize the Find operation by flattening the parent paths
    of nodes in a Disjoint Set.

Approach:
    1. If a node is its own parent, return it as the representative.
    2. Otherwise, recursively find the representative of its parent.
    3. Update the node's parent directly to the representative,
       compressing the path for future Find operations.
    4. Combine path compression with Union by Rank to keep the
       disjoint-set trees balanced.

Time Complexity:
    Find:  O(α(N)) amortized when combined with Union by Rank.
    Union: O(α(N)) amortized when combined with Union by Rank.

Space Complexity: O(N) for the parent and rank arrays, with
                  O(log N) worst-case recursion depth when the
                  trees are maintained using Union by Rank.
"""

def disjointSet(n):
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    def find(x):
        if parent[x] == x:
            return x

        parent[x] = find(parent[x])
        return parent[x]

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