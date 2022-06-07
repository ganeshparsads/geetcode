class Solution:
    def coinChange(self, coins, amount: int) -> int:
        memo = [amount + 1] * (amount + 1)

        # base case
        memo[0] = 0

        # top down approach
        for i in range(1, amount+1):
                for c in coins:
                    if i - c >= 0:
                        memo[i] = min(memo[i], 1 + memo[i-c])

        return memo[amount] if memo[amount] != (amount + 1) else -1

obj = Solution()

print(obj.coinChange([1, 2, 5], 11))
