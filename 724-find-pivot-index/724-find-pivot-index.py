class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lSum = 0
        rSum = sum(nums)
        
        for idx, i in enumerate(nums):
            rSum = rSum - i
            
            if idx != 0:
                lSum = lSum + nums[idx-1]
            
            if rSum == lSum:
                return idx
        
        return -1

