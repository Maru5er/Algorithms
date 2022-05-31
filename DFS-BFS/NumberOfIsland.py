class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        island = 0
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        if not grid:
            return 0
        
        def bfs(r, c):
            
            if grid[r][c] != "1":
                return
            
            grid[r][c] = "2"
            
            for dr, dc in directions:
                rows, cols = r + dr, c + dc
                if rows in range(row) and cols in range(col) and grid[rows][cols] == "1":
                        bfs(rows, cols)
