class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        normal = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        while True:
            slow = nums[slow]
            normal = nums[normal]
            
            
            if normal == slow:
                return normal
        
            
