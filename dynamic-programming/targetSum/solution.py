class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        
        arrSum = sum(nums)

        if arrSum < abs(target) or (target + arrSum) % 2 != 0:
            return 0

        subsetSum = (arrSum - target) // 2

        return countSubSetSum(nums, subsetSum)


    def countSubSetSum(self, nums, subsetSum: int) -> int:
        arrLen = len(nums)
        dp = [[0 for x in range(subsetSum + 1)] for x in range(arrLen + 1)]


        for i in range(arrLen+1):
            for j in range(subsetSum+1):
                # no element 
                if i == 0 and j > 0:
                    dp[i][j] = 0

                elif j == 0:
                    dp[i][j] = 1

                elif nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i-1]]

                else:
                    dp[i][j] = dp[i-1][j]

        print(dp)

        return dp[arrLen][subsetSum]

obj = Solution()

nums = [0, 1]

print(obj.countSubSetSum(nums, 1))
