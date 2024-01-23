class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n < 2:
            return nums[0]        
        
        dp = [0] * n

        dp[0] = nums[0]         
        res = dp[0]
        
        for idx in range(1, n):
            dp[idx] = max(nums[idx], nums[idx]+dp[idx-1])
            
            res = max(res, dp[idx])
        
        print(res)
        return res        