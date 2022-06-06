class Solution:
    def canPartition(self, nums) -> bool:
        size = len(nums)
        
        mean = sum(nums)

        if mean % 2 != 0:
            return False

        mean = int(mean/2)

        dp = [[False for x in range(mean + 1)] for x in range(size + 1)]
        
        for i in range(size+1):
            for j in range(mean+1):
                if i == 0:
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True
                
                if i == 0 and j == 0:
                    continue

                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j - nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        print(dp)
        return dp[size][mean]


obj = Solution()
print(obj.canPartition([1,2,5]))
