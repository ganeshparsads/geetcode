class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # for i in wordDict:
        #     if i in s:
        #         parts = s.split(i)
        #         s = ''.join(parts)
        # if s:
        #     return False
        # return True
        
#         sel = {}

#         string = ""

#         flag = False

#         for i in range(len(s)-1, -1, -1):
#             string =  s[i] + string

#             if string in wordDict:
#                 string = ""
#                 flag = True
#             else:
#                 flag = False

#         return flag
        dp = [False]*(len(s)+1)

        dp[len(s)] = True

        
        for i in range(len(s), -1, -1):
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]

                if dp[i]:
                    break

        return dp[0]

        
            
            