class Solution:
    def twoSum(self, nums, target):
        for cnt, val in enumerate(nums):
            if (val+val) == target:
                if nums.count(val) >= 2:
                    return cnt+1, nums.index((target-val), cnt+1) + 1

            elif nums.count(val) == 1 and (target-val) in nums:
                return cnt+1, nums.index((target-val))+1