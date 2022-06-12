class Solution:
    # recursion
    def minOperations(self, nums, x):
        totalSum = sum(nums)
        n = len(nums)
        if n <= 0:
            # Empty array
            return -1
        # If totalSum is less than target
        if totalSum < x:
            return -1
        # If totalSum is equal to target
        if totalSum == x:
            return n

        subarraySumToFind = totalSum - x
        left = 0
        currSum = 0

        result = 0
        # right pointer
        for right in range(n):
            currSum += nums[right]
            while currSum > subarraySumToFind:
                currSum -= nums[left]
                left += 1
            if currSum == subarraySumToFind:
                result = max(result, right - left + 1)

        ans = 0
        if result:
            ans = n - result
        else:
            ans = -1
        return ans