class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # visited = set()
        # for i in nums:
        #     if i in visited:
        #         return i
        #     visited.add(i)
        # return -1
        
#         n = len(nums) - 1
# 		# gives the maximum binary length of a number in [1,n]
#         max_length = n.bit_length()
#         ans = 0
        
#         for j in range(max_length):
# 			# moves the bits in 1 j positons to the left
# 			# thus mask has a 1 in the j-th position and 0s everywhere else
#             mask = 1 << j
#             count = 0
#             for i in range(n + 1):
# 				# if nums[i] has a 1 in the j-th position
#                 if nums[i] & mask > 0:
#                     count += 1
# 				# if i has a 1 in the j-th position
#                 if i & mask > 0:
#                     count -= 1
# 			#if we found extra 1s in the j-th position add that bit to ans
#             if count > 0:
#                 ans |= mask
                    
#         return ans
        n = len(nums) - 1
        max_length = n.bit_length()
        
        ans = 0
        
        for j in range(max_length):
            mask = 1 << j
            count = 0
            for i in range(n+1):
                if nums[i] & mask:
                    count += 1
                if i & mask:
                    count -= 1
            
            print(count)
            if count > 0:
                ans = ans | mask
        
        return ans