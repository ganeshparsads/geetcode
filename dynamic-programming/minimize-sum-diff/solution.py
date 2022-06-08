import math

class Solution:
    def subSetSum(self, nums, k, arr_length):
        dp = [[False for x in range(k + 1)] for x in range(arr_length + 1)]

        for i in range(arr_length+1):
            for j in range(k+1):
                if i == 0 and j > 0:
                    dp[i][j] = False
                elif j == 0:
                    dp[i][j] = True
                elif nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp

    def minimumDifference(self, nums) -> int:

        max_sum = sum(nums)

        if max_sum == 0:
            return 0

        arr_length = len(nums)
        dp = self.subSetSum(nums, max_sum, arr_length)

        half_sum = int(max_sum/2)

        min_sum = math.inf

        print(dp[arr_length])

        for idx, val in enumerate(dp[arr_length]):
            if val:
                min_sum = min(min_sum, max_sum - 2*idx)

        return min_sum


obj = Solution()

print(obj.minimumDifference([2,-1,0,4,-2,-9]))
