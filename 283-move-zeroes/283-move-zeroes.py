class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0

        while i < len(nums) - 1:
            if nums[i] == 0:
                # keep the i in the same position until u find element apart from 0
                nums.pop(i)
                nums.append(0)
                count += 1
            else:
                i += 1

            if i + count >= len(nums):
                break

