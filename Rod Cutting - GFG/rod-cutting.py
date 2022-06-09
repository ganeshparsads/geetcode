#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        arr = [i for i in range(1,n+1)]
        t = [[0 for i in range(n+1)] for j in range(n+1)]
        for  i in range(n+1):
            for j in range(n+1):
                if i==0 or j==0:
                    t[i][j] = 0
                elif arr[i-1] <= j:
                    t[i][j] = max( (price[i-1]+t[i][j-arr[i-1]]), (t[i-1][j]) )
                else:
                    t[i][j] = t[i-1][j]
        return t[n][n]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends