class Solution:
    def __init__(self):
        self.result = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return self.result
        self.recursive(candidates, target, 0, [])
        return self.result
    
    def forLoopRecursion(self, candidates, target, index, path):
        # base
        if not target:
            self.result.append(list(path))
            return
        
        if target < 0:
            return

        # logic
        for i in range(index, len(candidates)):
            path.append(candidates[i])
            self.forLoopRecursion(candidates, target-candidates[i], i, path)
            path.pop()
    
    def recursive(self, candidates, target, index, path):
        # base case
        if not target:
            self.result.append(list(path))
            return

        if index == len(candidates) or target < 0:
            return

        # logic
#         # case 1: no choose
#         self.recursive(candidates, target, index+1, list(path))

#         # case 2: choice
#         path.append(candidates[index])
#         self.recursive(candidates, target - candidates[index], index, list(path))

#         # case 2: choice
#         path.append(candidates[index])
#         self.recursive(candidates, target - candidates[index], index, list(path))

#         # case 1: no choose
#         path.pop()
#         self.recursive(candidates, target, index+1, list(path))

        # case 1: no choose
        self.recursive(candidates, target, index+1, list(path))

        # case 2: choice
        path.append(candidates[index])
        self.recursive(candidates, target - candidates[index], index, list(path))
        path.pop()