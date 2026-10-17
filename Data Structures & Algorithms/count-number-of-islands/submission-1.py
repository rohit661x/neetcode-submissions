class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

        #G = (V,E)
        # V = each land cell represented by '1'
        # E = horizontally or vertically adjacent 1's 
        # WTS = number of islands = # of '1's

        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != '1':
                return
            grid[r][c] = '0'  # mark visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count