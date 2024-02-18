class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0 for i in range(n)]
        dp[0] = arr[0]
        
        for i in range(1, n):
            max_ele = arr[i]
            
            j = 1
            while j <= k and i-j+1 >= 0:
                max_ele = max(max_ele, arr[i-j+1])
                
                if i-j >= 0:
                    dp[i] = max(dp[i], max_ele * j + dp[i-j])
                else:
                    dp[i] = max(dp[i], max_ele*j)
                
                j += 1
        
        return dp[n-1]
