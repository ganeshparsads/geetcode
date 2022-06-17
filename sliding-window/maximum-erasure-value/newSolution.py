class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        left = 0
        d = {}
        totalSum = 0
        maxSum = 0
        
        for i in range(len(nums)):
            
            n = nums[i]
            
            if n in d and d[n] >= left:

                for j in range(left, d[n]+1):
                    totalSum -= nums[j]
                    
                left = d[n] + 1

            d[n] = i
            totalSum += n
            
            maxSum = max(maxSum, totalSum)
            
        return maxSum;