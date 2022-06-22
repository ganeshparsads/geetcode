from collections import deque

class Solution:
    cSum = 0

    def maxCoins(self, nums):
        dq = deque(nums)
        dq.append(1)
        dq.appendleft(1)

        l = len(nums)

        dp = [[-1 for x in range(l + 1)] for x in range(l + 1)]

        return self.chooseCoins(1, len(nums), dq, dp)

    def chooseCoins(self, start, end, nums, dp):
        if start > end:
            return 0

        if dp[start][end] != -1:
            return dp[start][end]

        maxi = 0

        for idx in range(start, end+1):
            val = nums[start-1]*nums[idx]*nums[end+1]
            val = self.chooseCoins(start, idx-1, nums, dp) + val + self.chooseCoins(idx+1, end, nums, dp)

            maxi = max(maxi, val)


        dp[start][end] = maxi

        return dp[start][end]

obj = Solution()
print(obj.maxCoins([3,1,5,8]))
