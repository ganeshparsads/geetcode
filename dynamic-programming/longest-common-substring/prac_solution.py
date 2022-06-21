class Solution:
    def longestCommonSubsequence(self, text1, text2):
        cnt = 0

        def lcs(n, m):
            if n == 0 or m == 0:
                return 0

            if text1[n-1] == text2[m-1]:
                return 1 + lcs(n-1, m-1)
            else:
                return max(lcs(n-1, m), lcs(n, m-1))

        return lcs(len(text1), len(text2))

text1 = "abcdefgh"
text2 = "abedhr"

print(Solution().longestCommonSubsequence(text1, text2))
