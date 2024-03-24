class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = nums[0]
        max_so_far = prev
        
        for i in range(1, len(nums)):
            if nums[i] + prev >= nums[i]:
                prev = nums[i] + prev
            else:
                prev = nums[i]
            
            max_so_far = max(max_so_far, prev)
        
        return max(max_so_far, prev)