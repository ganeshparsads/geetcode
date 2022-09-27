class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        if obstacleGrid[r-1][c-1] == 1:
            return 0
        
        dp = [[0 for j in range(c+1)] for i in range(r+1)]
        
        dp[r-1][c-1] = 1
        
        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                if i == r-1 and j == c-1:
                    continue
                
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]