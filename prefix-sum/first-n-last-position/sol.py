class Solution(object):
    def binarySearchMin(self, nums, target):
        start = 0
        end = len(nums) - 1
        minEle = 1000000
        while(start <= end):
            mid = start + (end-start)//2
            
            if nums[mid] < target:
                start = mid+1
            elif nums[mid] > target:
                end = mid-1
            elif nums[mid] == target:
                minEle = min(minEle, mid)
                end = mid-1
        
        return minEle

    def binarySearchMax(self, nums, target):
        start = 0
        end = len(nums) - 1
        maxEle = -1
        while(start <= end):
            mid = start + (end-start)//2
            
            if nums[mid] < target:
                start = mid+1
            elif nums[mid] > target:
                end = mid-1
            elif nums[mid] == target:
                maxEle = max(maxEle, mid)
                start = mid+1
        
        return maxEle
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print(self.binarySearchMin(nums, target))
        print(self.binarySearchMax(nums, target))
        
obj = Solution()
obj.searchRange([5,7,7,8,8,10], 8)
