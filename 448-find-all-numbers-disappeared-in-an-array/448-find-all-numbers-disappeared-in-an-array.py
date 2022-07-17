class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            idx = abs(i) - 1

            if nums[idx] > 0:
                nums[idx] *= -1

        res = []
        
        for idx, i in enumerate(nums):
            if i > 0:
                res.append(idx + 1)
        
        return res
            