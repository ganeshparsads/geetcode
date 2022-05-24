class Solution:
    def maxSlidingWindow(self, nums, k):
        start = 0
        end = 0
        pSum = 0
        maxSum = 0

        while (end < len(nums)):
            pSum += nums[end]
            if (end - start + 1) < k:
                end += 1
            else:
                maxSum = max(maxSum, pSum)
                pSum = pSum - nums[start]
                end += 1
                start += 1
        return maxSum
