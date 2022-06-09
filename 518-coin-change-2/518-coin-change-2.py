class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        size = len(coins)
        dp = [[0 for x in range(amount + 1)] for x in range(size + 1)]

        for i in range(size+1):
            for j in range(amount+1):
                if i == 0 and j > 0:
                    dp[i][j] = 0
                elif j == 0:
                    dp[i][j] = 1
                elif coins[i-1] <= j:
                    dp[i][j] = dp[i][j - coins[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[size][amount]