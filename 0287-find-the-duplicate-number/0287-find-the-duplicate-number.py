class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # if nums[i] < 1:
            #     return i
            index = abs(nums[i]) - 1
            if nums[index] < 1:
                return abs(nums[i])
            nums[index] = -nums[index]

#         slow = 0
#         fast = 0
#         normal = 0
        
#         while True:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
            
#             if slow == fast:
#                 break
        
#         while True:
#             slow = nums[slow]
#             normal = nums[normal]
            
            
#             if normal == slow:
#                 return normal
        
            
