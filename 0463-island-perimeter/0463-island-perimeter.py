class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0

        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    peri += 4
                    
                    if i > 0 and grid[i-1][j]:
                        peri -= 2
                    if j > 0 and grid[i][j-1]:
                        peri -= 2
        
        return peri