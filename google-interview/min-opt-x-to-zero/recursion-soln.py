from collections import deque

class Solution:
    # recursion
    def minOperations(self, nums, x):
        arr_sum = sum(nums)
        if arr_sum < x:
            return -1

        def solve(n_nums, remaining_Sum):
            # base case
            if remaining_Sum == 0:
                return 0

            if not n_nums:
                return 1000000                

            if remaining_Sum < 0:
                return 1000000

            left = 1 + solve(n_nums[1:], remaining_Sum - n_nums[0])
            right = 1 + solve(n_nums[:-1], remaining_Sum - n_nums[-1])

            return min(left, right)

        soln = solve(nums, x)

        if soln == 1000001:
            return -1
        else:
            return soln

obj = Solution()

print("answer: ", obj.minOperations([1,1,4,2,3], 10))
print("answer: ", obj.minOperations([5,6,7,8,9], 4))
print("answer: ", obj.minOperations([3,2,20,1,1,3], 10))
