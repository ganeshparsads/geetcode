class Solution:
    def maxSubArray(self, nums):
        start = 0
        end = 0

        size = len(nums)
        incSum = 0
        maxSum = 0

        while end < size:

            if (incSum + nums[end]) < incSum:
                incSum += nums[end]
                end += 1
            else:
                maxSum = max(maxSum, incSum)
                print(start)
                incSum -= nums[start]
                start += 1

        return maxSum

obj = Solution()

print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
