#User function Template for python3

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

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends