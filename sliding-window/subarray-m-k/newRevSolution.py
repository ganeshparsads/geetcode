class Solution:
    def subarraySum(self, nums, k):
        start = end = len(nums)
        wSum = 0
        cnt = 0

        while start >= 0:
            wSum += nums[start]

            if wSum == k:
                cnt += 1
                wSum -
                start -= 1
                end -= 1


obj = Solution()

print(obj.subarraySum([1,2,1,2,1], 3))