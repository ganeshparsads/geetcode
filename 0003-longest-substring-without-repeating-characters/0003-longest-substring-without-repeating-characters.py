class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = r = 0
        
        res = 0
        
        n = len(s)
        
        while r < n:
            if s[r] in window:
                res = max(res, len(window))
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            r += 1
        
        res = max(res, len(window))
        
        return res
            