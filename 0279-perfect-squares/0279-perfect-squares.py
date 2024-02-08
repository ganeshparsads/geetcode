class Solution:
    def numSquares(self, n: int) -> int:
        sqrs = [i**2 for i in range(1,int(math.sqrt(n) +  1))]
        dp = [n+1]*(n+1)
        dp[0] = 0

        for i in range(1,n+1):
            for s in sqrs:
                if i - s >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-s])
        return dp[-1]