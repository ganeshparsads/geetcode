class Solution:
    def __init__(self):
        self.result = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return self.result
        self.recursive(candidates, target, 0, [])
        return self.result
    
    def recursive(self, candidates, target, index, path):
        # base case
        if not target:
            self.result.append(path)
            return

        if index == len(candidates) or target < 0:
            return

        # logic
        # case 1: no choose
        self.recursive(candidates, target, index+1, list(path))

        # case 2: choice
        path.append(candidates[index])
        self.recursive(candidates, target - candidates[index], index, list(path))