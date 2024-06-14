class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        n = len(s)
        
        data = {}
        max_freq = -1
        result = 0
        
        while r < n:
            if s[r] not in data:
                data[s[r]] = 1
            else:
                data[s[r]] += 1
            
            max_freq = max(max_freq, data[s[r]])
            
            while (r-l+1) - max_freq > k:
                data[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
            r += 1
        
        return result