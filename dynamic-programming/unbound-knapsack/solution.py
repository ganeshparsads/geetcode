class Solution:
    def knapSack(self, N, W, val, wt):
        # code here

        C = [0]*(W+1)

        for w in range(W+1):
            wMax = 0
            for idx, v in enumerate(wt):
                if v <= w:
                    wMax = max(wMax, val[idx] + C[w-v])

            C[w] = wMax

        return C[W]

N = 4
W = 8

val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]

obj = Solution()

print(obj.knapSack(N, W, val, wt))
