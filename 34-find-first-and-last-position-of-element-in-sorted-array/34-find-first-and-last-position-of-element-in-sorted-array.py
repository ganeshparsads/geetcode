class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right-left)//2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        first = search(target)
        last = search(target + 1) - 1
        if target in nums[first: first+1]:
            return [first, last]
        else:
            return [-1, -1]
