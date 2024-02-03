class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = {n : 0}

        for i in range(n-1, -1, -1):
            maxNum, dp[i], j, limit = float('-inf'), float('-inf'), i, i + k
            while j < n and j < limit:
                maxNum = max(maxNum, arr[j])
                dp[i] = max(dp[i], ((j-i+1) * maxNum) + dp[j+1])
                j += 1
        
        return dp[0]        