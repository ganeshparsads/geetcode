class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False]*(len(s)+1)
        results = {}

        dp[len(s)] = True

        print(len(s))

        for i in range(len(s)-1, -1, -1):
            results[i] = []
            for word in wordDict:
                # if s[i:i+len(word)] == "andd":
                #     import pdb
                #     pdb.set_trace()
                if len(word) + i <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]

                    if dp[i]:
                        results[i].append(s[i:i+len(word)])
                    # print(w)
                    # results[i] = (w + " " + results[i+len(w)]).strip()

                # if dp[i]:
                #     break

        print(dp)
        print(results)

        return dp[0]


obj = Solution()

s = "pineapplepenapple"

wordDict = ["apple","pen","applepen","pine","pineapple"]

print(obj.wordBreak(s, wordDict))
