class Solution:
    def cutRod(self, price, n):
        dp = [[0 for x in range(n+1)] for x in range(n + 1)]
        arr = [i for i in range(1,n+1)]
        for i in range(1, n+1):
          for j in range(1, n+1):
            if i <= j:
              dp[i][j] = max(price[i-1] + dp[i][j-i], dp[i-1][j])
            else:
              dp[i][j] = dp[i-1][j]

        return dp[n][n]


obj = Solution()

price = [1, 5, 8, 9, 10, 17, 17, 20]

print(obj.cutRod(price, 8))
