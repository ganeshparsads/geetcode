class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1 for x in range(numRows)] for x in range(numRows)]
        
        for i in range(numRows):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

            dp[i] = dp[i][:(i+1)]


        return dp
