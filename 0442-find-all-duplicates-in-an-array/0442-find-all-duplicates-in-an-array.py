class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        
        for idx in range(len(nums)):
            val = abs(nums[idx])
            
            if nums[val-1] < 1:
                ans.append(val)
            else:
                nums[val-1] = -nums[val-1]
            
        return ans