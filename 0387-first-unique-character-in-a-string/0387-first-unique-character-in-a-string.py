class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniq = Counter(s)
        
        for idx, val in enumerate(s):
            if uniq[val] == 1:
                return idx
        
        return -1
