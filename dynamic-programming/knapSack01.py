class Solution:

    #Function to return max value that can be put in knapsack of capacity W.
    # recursion soln
    # def knapSack(self,W, wt, val, n):
    #     if n == 0 or W <= 0:
    #         return 0

    #     if wt[n-1] <= W:
    #         return max(val[n-1] + self.knapSack(W-wt[n-1], wt, val, n-1), self.knapSack(W, wt, val, n-1))
    #     elif wt[n-1] > W:
    #         return self.knapSack(W, wt, val, n-1)


    # top down knapSack solution
    def knapSack(self,W, wt, val, n):
        dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

        for i in range(n+1):
            for j in range(W+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    continue

                if wt[i-1] <= j:
                    dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][W]

obj = Solution()

print(obj.knapSack(4, [4,5,1], [1,2,3], 3))
