class Solution:
    def __init__(self):
        self.result = []
    
    def letterCasePermutation(self, s: str) -> List[str]:
        self.result.append(s)
        s = list(s)
        self.backtrack(0, s)

        return self.result        

    def backtrack(self, start, s):
        # if start == len(s):
        #     return

        for i in range(start, len(s)):
            if s[i].isalpha():
                s[i] = chr(ord(s[i]) ^ 32)
                self.result.append(''.join(s))                
                self.backtrack(i + 1, s)
                s[i] = chr(ord(s[i]) ^ 32)

        # self.backtrack(len(s), s)