from collections import deque

class Solution:
    def maximumUniqueSubarray(self, nums):
        start = 0
        end = 0

        dq = []
        maxSum = 0
        windowSum = 0

        while end < len(nums):
            if nums[end] not in dq or not dq:
                windowSum += nums[end]
                dq.append(nums[end])
                end += 1
            else:
                maxSum = max(maxSum, windowSum)
                windowSum = windowSum - nums[start]
                start += 1

                dq = dq[nums.index(nums[end])+1:]
                windowSum = sum(dq)

        return max(maxSum, sum(dq))

obj = Solution()

print(obj.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))
