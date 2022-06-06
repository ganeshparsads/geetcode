class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                # keep the i in the same position until u find element apart from 0
                nums.remove(i)
                nums.append(0)

