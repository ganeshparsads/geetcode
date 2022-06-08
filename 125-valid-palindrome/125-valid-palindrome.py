class Solution:
    def isPalindrome(self, s: str) -> bool:
        # regex
        # s = re.sub('[^A-Za-z0-9]+', '', s.lower())
        # return s == s[::-1]
        
        # two pointers
        s = re.sub('[^A-Za-z0-9]+', '', s.lower())
        i = 0
        j = len(s) - 1
        
        for i in range(len(s)//2):
            if i != j and s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1


        return True
