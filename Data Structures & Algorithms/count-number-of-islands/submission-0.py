class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

        #G = (V,E)
        # V = each land cell represented by '1'
        # E = horizontally or vertically adjacent 1's 
        # WTS = number of islands = # of '1's

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        def dfs(r, c):
            if ( 
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or grid [r][c] == "0"
                or (r,c) in visited
            ):
                return 
            
            visited.add((r,c))

            dfs(r + 1, c) #down
            dfs(r - 1, c) #up
            dfs(r, c + 1) #right
            dfs(r, c - 1) #left
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    dfs(r,c)
        return islands