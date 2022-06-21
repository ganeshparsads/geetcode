class Solution:
    # recursion
    # def longestCommonSubsequence(self, text1, text2):
    #     len1 = len(text1)
    #     len2 = len(text2)
        
    #     def lcs(n, m):
    #         if m == 0 or n == 0:
    #             return 0
            
    #         if text1[n-1] == text2[m-1]:
    #             return 1 + lcs(n-1, m-1)
    #         else:
    #             return max(lcs(n-1, m), lcs(n, m-1))

    #     return lcs(len1, len2)


    # as we have seen the pattern n depends on n-1 we can easily write top-down.
    # top down approach
    def longestCommonSubsequence(self, text1, text2):
        len1 = len(text1)
        len2 = len(text2)

        memo = [[0 for i in range(len2+1)] for j in range(len1+1)]

        cnt = 0
        maxCnt = 0

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if text1[i-1] == text2[j-1]:
                    memo[i][j] = 1 + memo[i-1][j-1]
                    print("Hi")
                    cnt += 1
                else:
                    print("Hello")
                    maxCnt = max(maxCnt, cnt)
                    cnt = 0
                    memo[i][j] = max(memo[i][j-1], memo[i-1][j])

        maxCnt = max(maxCnt, cnt)

        print(maxCnt)

        return memo[len1][len2]

    # bottom up
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     matrix = [[0]*(len(text2)+1) for i in range(len(text1)+1) ]
    #     for i in range(len(text1)-1,-1,-1):
    #         for j in range(len(text2)-1,-1,-1):
    #             if(text1[i]==text2[j]):
    #                 matrix[i][j] = 1 + matrix[i+1][j+1]
    #             else:
    #                 matrix[i][j] = max(matrix[i+1][j],matrix[i][j+1])
    #     return matrix[0][0]

text1 = "abcdefgh"
text2 = "abcedhr"

print(Solution().longestCommonSubsequence(text1, text2))
