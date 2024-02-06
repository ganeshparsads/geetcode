class Solution:
    def __init__(self):
        self.result = []
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.forLoopHelper(candidates, 0, target, [])
        return self.result

    def forLoopHelper(self, candidates, pivot, target, path):
        # base
        if target < 0:
            return
        if target == 0:
            self.result.append(path)
            return
        
        # logic
        for i in range(pivot, len(candidates)):
            path.append(candidates[i])
            self.forLoopHelper(candidates, i, target-candidates[i], list(path))
            path.pop()

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
