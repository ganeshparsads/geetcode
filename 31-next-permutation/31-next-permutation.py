class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        findEle = -1
        
        for i in range(n-1, -1, -1):
            if nums[i-1] < nums[i]:
                findEle = i-1
                break
        
        if findEle < 0:
            nums.reverse()
        else:
            for j in range(n-1, -1, -1):
                if nums[j] > nums[findEle]:
                    break
            nums[j], nums[findEle] = nums[findEle], nums[j]
            
            nums[findEle+1:] = reversed(nums[findEle+1:])
