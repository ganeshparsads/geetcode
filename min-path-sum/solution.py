class Solution:
    def minPathSum(self, grid):
        
        # [[False for x in range(mean + 1)] for x in range(size + 1)]
        dp = [[0 for x in range(len(grid[0]))] for x in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                # initialization:
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                # optimal decision
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[len(grid)-1][len(grid[0])-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]

obj = Solution()
print(obj.minPathSum(grid))
