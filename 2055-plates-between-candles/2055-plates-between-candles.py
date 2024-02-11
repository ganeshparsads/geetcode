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
        # left_candle[0] = 0 if s[0] == "|" else -1
        for i in range(len(s)):
            if s[i] == "|":
                left_candle[i] = i
            else:
                left_candle[i] = left_candle[i-1]
                
        right_candle = [-1 for i in range(len(s))]
        right_candle[-1] = len(s)-1 if s[-1] == "|" else -1
        for i in range(len(s)-2, -1, -1):
            if s[i] == "|":
                right_candle[i] = i
            else:
                right_candle[i] = right_candle[i+1]
                
        res = [0 for i in range(len(queries))]   
  
        ct = 0
        for i, j in queries:
            start = right_candle[i]
            end  = left_candle[j]
            print(start, end)
            if start >= end:
                res[ct] = 0
            else:
                val = prefix[end] - prefix[start]
                if val > 0:
                    res[ct] = val
                else:
                    res[ct] = 0
            ct += 1

        return res