class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []

        for idx, i in enumerate(nums):
            if idx == 0:
                dp.append(i)
            elif idx == 1:
                dp.append(max(i, dp[0]))
            else:
                dp.append(max(i+dp[idx-2], dp[idx-1]))

        return dp[len(nums)-1]
        