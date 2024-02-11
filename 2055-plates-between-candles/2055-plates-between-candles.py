class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [0 for i in range(len(s))]
        prefix[0] = 1 if s[0] == "*" else 0
        for i in range(1, len(s)):
            if s[i] == "*":
                prefix[i] = 1 + prefix[i-1]
            else:
                prefix[i] = prefix[i-1]

        left_candle = [-1 for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == "|":
                left_candle[i] = i
            else:
                left_candle[i] = left_candle[i-1]
                
        right_candle = [-1 for i in range(len(s))]
        rightMost = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] == "|":
                rightMost = i
            right_candle[i] = rightMost
                
        res = []

        for i, j in queries:
            start = right_candle[i]
            end  = left_candle[j]
            if i == j or start >= end:
                res.append(0)
            else:
                val = prefix[end] - prefix[start]
                res.append(val)

        return res