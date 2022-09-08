class Solution:
    def longestPalindrome(self, s: str) -> int:
        dupSet = set()
        for i in list(s):
            if i not in dupSet:
                dupSet.add(i)
            else:
                dupSet.remove(i)
        
        if len(dupSet):
            return len(s) - (len(dupSet) - 1)

        return len(s)