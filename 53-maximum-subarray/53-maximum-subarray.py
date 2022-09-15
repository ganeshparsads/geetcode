class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        left = 0
        right = 0
        
        maxSum = nums[0]
        rSum = nums[0]
        
        for i in nums[1:]:
            rSum = max(i, rSum+i)
            maxSum  = max(maxSum, rSum)
        
        return maxSum