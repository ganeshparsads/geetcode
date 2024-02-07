class Solution:
    def __init__(self):
        self.result = []
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backTrack(nums, 0, [])
        return self.result
    
    def backTrack(self, nums, index, path):
        # base
        if index == len(nums):
            self.result.append(path)
            return

        # logic
        # not choose
        self.backTrack(nums, index+1, path)
        
        path.append(nums[index])
        # choose
        self.backTrack(nums, index+1, list(path))
        
        path.pop()
