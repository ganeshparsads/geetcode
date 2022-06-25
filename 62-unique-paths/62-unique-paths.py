class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # [[False for x in range(mean + 1)] for x in range(size + 1)]
        dp = [[0 for x in range(n)] for x in range(m)]

        for i in range(m):
            for j in range(n):

                # initialization:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                # optimal decision
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]