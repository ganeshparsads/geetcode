class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        d = {(rows-1,cols-1):grid[-1][-1]}

        def dfs(row, col):

            if (row,col) in d: return d[(row, col)]

            if row<rows-1 and col<cols-1:
                d[(row, col)] =  grid[row][col] + min(dfs(row+1, col), dfs(row, col+1))
                return d[(row, col)]
            elif row==rows-1:
                d[(row, col)] = grid[row][col] + dfs(row, col+1)
                return d[(row, col)]
            elif col==cols-1:
                d[(row, col)] = grid[row][col] + dfs(row+1, col)
                return d[(row, col)]

        return dfs(0,0)