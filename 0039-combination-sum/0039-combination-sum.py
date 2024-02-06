class Solution:
    def __init__(self):
        self.result = []
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.helper(candidates, 0, target, [])
        return self.result
    
    def helper(self, candidates, index, target, path):
        # base
        if index == len(candidates) or target < 0:
            return
        if target == 0:
            self.result.append(path)
            return
        
        # logic

        # choose
        path.append(candidates[index])
        self.helper(candidates, index, target - candidates[index], list(path))
        path.pop()
        # not choose
        self.helper(candidates, index+1, target, path)        
