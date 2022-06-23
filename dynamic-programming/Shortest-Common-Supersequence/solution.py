class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        memo = [[0 for i in range(len2+1)] for j in range(len1+1)]

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if str1[i-1] == str2[j-1]:
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = max(memo[i][j-1], memo[i-1][j])

        i = len1
        j = len2

        choices = []

        while  i > 0 and j > 0:
            if str1[i-1] ==  str2[j-1]:
                choices.append(str1[i-1])
                i -= 1
                j -= 1
            else:
                print(str1[i-1], str2[j-1])
                if memo[i-1][j] > memo[i][j-1]:
                    choices.append(str1[i-1])
                    i -= 1
                else:
                    choices.append(str2[j-1])
                    j -= 1

        while i > 0:
            choices.append(str1[i-1])
            i -= 1

        while j > 0:
            choices.append(str2[j-1])
            j -= 1

        choices.reverse()

        return ''.join(choices)

obj = Solution()

print(obj.shortestCommonSupersequence("zabac", "bcab"))
