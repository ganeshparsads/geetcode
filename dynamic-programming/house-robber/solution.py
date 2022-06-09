class Solution:
    def rob(self, nums):
        dp = []

        for index, i in enumerate(nums):
            idx = index
            if idx == 0:
                dp.append(i)
            elif idx == 1:
                # always keep max on the odd index like 1, 3, 5
                # where 0, 2, 4 are wrong window.
                # bcz if uve 2 elements in that also it'll need max to come out.
                dp.append(max(i, dp[0]))
            else:
                dp.append(max(i+dp[idx-2], dp[idx-1]))

        return dp[len(nums)-1]


obj = Solution()

print(obj.rob([2, 1, 1, 2]))
