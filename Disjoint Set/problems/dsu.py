"""
Disjoint Set (Union-Find)

Problem:
    Given n elements numbered from 1 to n, process two types
    of queries:
        Type 1: [1, x, z] -> Merge the group containing x into
                            the group containing z.
        Type 2: [2, x]    -> Find the representative of x.

Approach:
    1. Initially, each element is its own representative.
    2. Use Find with path compression to locate the root.
    3. During Union, make the root of x point to the root of z,
       preserving the required representative direction.

Time Complexity:
    Find:  O(N) worst case for an individual operation in
           general, with path compression improving repeated finds.
    Union: O(N) worst case, due to the Find operations.

Space Complexity: O(N) for the parent array, excluding output.
"""

def disjointSet(n, queries):
    parent = [i for i in range(n + 1)]
    op = []

    def find(x):
        if parent[x] == x:
            return x

        parent[x] = find(parent[x])

        return parent[x]

    def union(x, z):
        x_rep = find(x)
        z_rep = find(z)

        if x_rep == z_rep:
            return

        parent[x_rep] = z_rep

    for query in queries:
        if query[0] == 1:
            _, x, z = query
            union(x, z)
        elif query[0] == 2:
            x = query[1]
            rep = find(x)
            op.append(rep)

    return op