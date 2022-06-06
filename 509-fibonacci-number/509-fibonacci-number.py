class Solution:
    def fib(self, n: int) -> int:
        memo = []
        
        memo.append(0)
        
        for i in range(1, n+1):
            if i == 1:
                memo.append(1)
            elif i == 2:
                memo.append(1)
            else:
                memo.append(memo[i-1] + memo[i-2])
        
        return memo[n]        