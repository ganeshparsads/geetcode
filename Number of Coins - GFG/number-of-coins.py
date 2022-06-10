#User function Template for python3
class Solution:
	def minCoins(self, coins, M, amount):
		# code here
        memo = [amount + 1] * (amount + 1)

        # base case
        memo[0] = 0

        for i in range(1, amount+1):
                for c in coins:
                    if i - c >= 0:
                        memo[i] = min(memo[i], 1 + memo[i-c])

        return memo[amount] if memo[amount] != (amount + 1) else -1		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends