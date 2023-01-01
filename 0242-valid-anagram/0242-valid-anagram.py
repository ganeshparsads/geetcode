from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = [0 for i in range(26)]
        s2 = [0 for i in range(26)]
        
        for i in list(s):
            asci = ord(i) - 97
            s1[asci] += 1

        for i in list(t):
            asci = ord(i) - 97
            s2[asci] += 1
        
        for i in range(26):
            if s1[i] != s2[i]:
                return False

        return True