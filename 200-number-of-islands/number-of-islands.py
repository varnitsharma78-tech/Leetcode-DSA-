class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        
        def dfs(r, c):
            # Base case: boundary check and water check
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
                return
                
            # Mark the cell as visited by turning it into water ("0")
            grid[r][c] = "0"
            
            # Recursively explore all 4 adjacent directions
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left

        # Scan every cell in the 2D grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # Found a new island, trigger DFS to sink it
                    num_islands += 1
                    dfs(r, c)
                    
        return num_islands
