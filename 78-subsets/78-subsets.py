class Solution:
    def __init__(self):
        self.result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return self.result

        self.helper(nums, 0, [])
        self.result.append([])
        return self.result
    
    def helper(self, nums, index, previous):
        if index >= len(nums):
            return
        for i in range(index, len(nums)):
            parent = previous + [nums[i]]
            self.result.append(parent)
            self.helper(nums, i+1, parent)
