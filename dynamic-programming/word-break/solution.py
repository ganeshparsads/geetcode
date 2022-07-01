class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False]*(len(s)+1)

        dp[len(s)] = True

        # traversing from the last to the start
        for i in range(len(s), -1, -1):
            for w in wordDict:
                # if it matches with current word check for subtracting 
                # this word
                # rest is also solved.
                if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]

                if dp[i]:
                    break

        return dp[0]
