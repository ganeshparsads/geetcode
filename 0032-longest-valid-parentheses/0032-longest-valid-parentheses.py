class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = 0
        l_count = r_count = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                l_count += 1
            else:
                r_count += 1
            
            if r_count == l_count:
                result = max(result, 2*l_count)
            if r_count > l_count:
                l_count = r_count = 0
        
        i = len(s) - 1
        l_count = r_count = 0
        
        while i >= 0:
            if s[i] == "(":
                l_count += 1
            else:
                r_count += 1
            
            if r_count == l_count:
                result = max(result, 2*l_count)
            if l_count > r_count:
                l_count = r_count = 0
            
            i -= 1

        
        return result
            