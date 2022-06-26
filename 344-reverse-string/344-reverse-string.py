from math import ceil, floor

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        start = floor(n/2.0) - 1
        end = ceil(n/2.0)        
        # if n%2:
        #     start -= 1
        
        
        while start >= 0:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start -= 1
            end += 1
            
        return s
            
        