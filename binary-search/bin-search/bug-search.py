class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return
        
        rep = len(nums)//2
        
        if nums[rep] == target:
            return rep
        
        elif target <= nums[rep]:
            return self.search(nums[:rep], target)

        elif target >= nums[rep]:
            return (rep + self.search(nums[rep:], target))
        
        else:
            return -1

obj = Solution()

print(obj.search([-1,0,3,5,9,12], 9))