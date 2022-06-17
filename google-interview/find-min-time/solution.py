import math

class Solution:
    def minTime(self, S1, S2, N):
        # code here

        ans = min(s1, s2) * N

        for i in range(N+1):
            stage = max(S1*i, S2*(N-i))
            ans = min(ans, stage)

        return ans
