class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        #Return the maximum area of an island in grid. If there is no island, return 0.
        #vertical & horizontal, diagonal does not count

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        max_area = 0

        directions = [(1,0), (-1, 0), (0,1), (0, -1)]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1 and (r, c) not in visited:
                    queue = deque([(r, c)])
                    visited.add((r,c))
                    area = 0 
                
                    while queue:

                        row, col = queue.popleft()
                        area += 1

                        for dr, dc in directions:
                            nr = row + dr
                            nc = col + dc

                            if ((0 <= nr < rows and 0 <= nc < cols)
                            and grid[nr][nc] == 1 
                            and (nr,nc) not in visited ):

                                visited.add((nr, nc))
                                queue.append((nr, nc)) 
                    max_area = max(max_area, area)
        return max_area