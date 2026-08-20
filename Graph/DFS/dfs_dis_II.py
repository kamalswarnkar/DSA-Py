"""
Counting Islands using DFS

A grid can be treated as an implicit graph where each land cell
represents a vertex and adjacent land cells represent connections.

Since an island is a connected group of land cells, counting islands
is equivalent to counting the connected components of the grid.

For every unvisited land cell:
1. Count it as a new island.
2. Start DFS from that cell.
3. Visit all connected land cells in all 8 directions.
4. Continue until every cell has been checked.

Directions considered:
    • Up
    • Down
    • Left
    • Right
    • Four diagonals

Time Complexity:
    O(N × M)

Space Complexity:
    O(N × M)

where,
N = number of rows
M = number of columns

Note:
• Uses DFS to find connected components.
• Diagonal connections are also considered.
• Each land cell is visited exactly once.
"""


def dfs(adj, r, c, vis, direc):
    row = len(adj)
    col = len(adj[0])
        
    vis[r][c] = True # Mark the current land cell as visited.
        
    for dr, dc in direc: # Explore all 8 possible directions.
        nr = r + dr
        nc = c + dc
            
        if (0 <= nr < row) and (0 <= nc < col) and adj[nr][nc] == 'L' and (not vis[nr][nc]):
            dfs(adj, nr, nc, vis, direc)
    
def countIslands(self, grid):
    row = len(grid)
    col = len(grid[0])
        
    visited = [[False] * col for _  in range(row)]
    direction = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0),   (1, 1)
    ]
    count = 0
        
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 'L' and not visited[r][c]: # Every unvisited land cell starts a new connected component (island).
                count += 1
                dfs(grid, r, c, visited, direction)
        
    return count