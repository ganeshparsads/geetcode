class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        ans = 0 
        stack = []
        for x in nums: 
            val = 1
            while stack and stack[-1][0] <= x: 
                val = max(val, stack.pop()[1]+1)
            if not stack: 
                val = 0
            stack.append((x, val))
            ans = max(ans, val)
        return ans 