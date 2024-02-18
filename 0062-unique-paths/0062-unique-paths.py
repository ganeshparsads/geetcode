class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        
        # last column
        for i in range(m):
            dp[i][n-1] = 1
            
        # last row
        for j in range(n):
            dp[m-1][j] = 1
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i][j+1] + dp[i+1][j]
        
        return dp[0][0]        
        
        # recursion
#         return self.helper(0, 0, m, n)
    
#     def helper(self, row, col, m, n):
#         # base
#         if row >= m or col >= n:
#             return 0
#         if row == m-1 and col == n-1:
#             return 1
        
#         # logic
#         right = self.helper(row, col+1, m, n)
#         bottom = self.helper(row+1, col, m, n)
        
#         return right + botto