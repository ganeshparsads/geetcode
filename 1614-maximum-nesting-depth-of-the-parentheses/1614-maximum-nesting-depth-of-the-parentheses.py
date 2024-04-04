class Solution:
    def maxDepth(self, s: str) -> int:
        maxResult = 0
        
        res = 0
        
        for i in s:
            if i == "(":
                res += 1
            elif i == ")":
                res -= 1
            
            maxResult = max(maxResult, res)
        
        return maxResult