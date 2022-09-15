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
        
        return nums
        
        
        
        n=len(nums)
        tmp2=0
        tmp=-1
        
        # find the decreased from behind
        for i in range(n-1,-1,-1):
            if nums[i-1]<nums[i]:
                tmp=i-1
                break
        if tmp<0:
            nums.reverse()
        else:
            # find the immediate increase element to swap with
            for j in range(n-1,-1,-1):
                if nums[j]>nums[tmp]:
                    tmp2=j
                    break
            
            # swap the j with i
            nums[j],nums[tmp]=nums[tmp],nums[j]
            
            # reverse the rest of the array from i
            nums[tmp+1:]=reversed(nums[tmp+1:])
        return nums