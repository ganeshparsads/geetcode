class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = len(nums)

        while(maxNum):
            if maxNum not in nums:
                return maxNum
            maxNum = maxNum - 1

        return maxNum
