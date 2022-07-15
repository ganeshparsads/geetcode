class Solution:
    def pivotIndex(self, nums):
        lSum = 0
        rSum = sum(nums)
        
        for idx, i in enumerate(nums):
            rSum = rSum - i
            
            if idx != 0:
                lSum = lSum + nums[idx-1]
            
            if rSum == lSum:
                return idx
        
        return -1


obj = Solution()

print(obj.pivotIndex([1,7,3,6,5,6]))
