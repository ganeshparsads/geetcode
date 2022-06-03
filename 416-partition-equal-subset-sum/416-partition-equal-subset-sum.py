class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        size = len(nums)
        
        mean = sum(nums) / 2.0
        
        print(mean)
        
        if mean > 1 and mean % int(mean) != 0 or mean < 1:
            return False

        mean = int(mean)

        dp = [[-1 for x in range(mean + 1)] for x in range(size + 1)]
        
        for i in range(size+1):
            for j in range(mean+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    continue
                
                if nums[i-1] <= j:
                    dp[i][j] = max(nums[i-1] + dp[i-1][j - nums[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        print(dp[size][mean])
        if dp[size][mean] == mean:
            return True

        return False