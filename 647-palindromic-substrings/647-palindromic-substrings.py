class Solution:
    def countSubstrings(self, S):
        res = 0
        n = len(S)
        for i in range(n):
            left = i
            right = i
            while left >= 0 and right < n and S[left] == S[right]:
                res += 1
                left -= 1
                right += 1

        for i in range(n):
            left = i
            right = i+1
            while left >= 0 and right < n and S[left] == S[right]:
                res += 1
                left -= 1
                right += 1
        
        return res