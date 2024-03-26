class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        nums = list(set(nums))
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1

        for i in range(n):
            if abs(nums[i]) <= n:
                nums[abs(nums[i])-1] *= -1

        for i in range(n):
            if nums[i] > 0:
                return i+1

        return n+1