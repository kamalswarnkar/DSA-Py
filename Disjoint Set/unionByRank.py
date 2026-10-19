"""
Union By Rank Implementation
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
