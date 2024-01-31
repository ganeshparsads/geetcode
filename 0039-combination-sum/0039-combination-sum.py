from copy import deepcopy

class Solution:
    def __init__(self):
        self.result = []
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backTrack(candidates, target, 0, [])
        
        return self.result

    def backTrack(self, candidates, target, idx, path):
        
        # base
        if target < 0 or idx == len(candidates):
            return
        
        if target == 0:
            self.result.append(path)
            return

        #logic
        
        # not choose
        self.backTrack(candidates, target, idx+1, list(path))
        
        # choose
        path.append(candidates[idx])
        self.backTrack(candidates, target-candidates[idx], idx, list(path))
