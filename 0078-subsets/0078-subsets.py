class Solution:
    def __init__(self):
        self.result = []
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # self.forLoop(nums, 0, [])
        self.result.append([])
        for i in nums:
            for j in range(len(self.result)):
                temp = list(self.result[j])
                temp.append(i)
                self.result.append(temp)
        
        
        return self.result
    
    def forLoop(self, nums, pivot, path):
        self.result.append(path)

        for i in range(pivot, len(nums)):
            path.append(nums[i])
            self.forLoop(nums, i+1, list(path))
            path.pop()
    
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
