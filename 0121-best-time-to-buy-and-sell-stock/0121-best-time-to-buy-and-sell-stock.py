class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_so_far = prices[-1]

        profit = 0
        
        for i in range(len(prices)-1, -1, -1):
            if max_so_far < prices[i]:
                max_so_far = prices[i]
            else:
                profit = max(profit, (max_so_far - prices[i]))
        
        return profit