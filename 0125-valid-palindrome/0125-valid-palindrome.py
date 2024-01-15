import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]+', '', s.lower())
        i = 0
        j = len(s) - 1
        
        for i in range(len(s)//2):
            if i != j and s[i] != s[j]:
                return False
            
            i += 1
            j -= 1


        return True