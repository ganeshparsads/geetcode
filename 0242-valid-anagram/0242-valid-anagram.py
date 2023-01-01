from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # n logn
        # return sorted(list(s)) == sorted(list(t))

        s1 = Counter(s)
        s2 = Counter(t)
        
        if len(s1) != len(s2):
            return False
        
        for key, val in s1.items():
            if key in s2 and s1[key] == s2[key]:
                continue
            else:
                return False
        
        return True