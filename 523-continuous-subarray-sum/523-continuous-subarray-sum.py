from collections import defaultdict

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = [nums[0]] # generate prefix sums
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i]+prefix_sum[-1])
        
        remainders = {} # store remainder:index pairs
        for i,val in enumerate(prefix_sum):
            remainder = val%k
            
            if remainder==0 and i>0: # remainder=0 at i=0 means that the subarray is not at least len=2, so need the i>0 check
                return True
            
            if remainder in remainders:
                if i-remainders[remainder]>1: # same remainder next to each other implies subarray with len<2, so need the >1 check
                    return True
            else:
                remainders[remainder] = i
            
        return False
#         prefix_sum = [0 for i in range(len(nums))]
        
#         hMap = defaultdict(int)
#         hMap[0] += 1

#         # import pdb
#         # pdb.set_trace()
        
#         for idx, i in enumerate(nums):
#             if idx == 0:
#                 prefix_sum[idx] = i
#             else:
#                 prefix_sum[idx] = prefix_sum[idx-1] + i
            
#             if i % k != 0:
#                 new_sum = 10000000
#                 m = 0

#                 if prefix_sum[idx] % k == 0:
#                     return True

#                 while new_sum > nums[0]:
#                     new_sum = prefix_sum[idx] - m*k
#                     if new_sum in hMap:
#                         return True
#                     m += 1

#             hMap[prefix_sum[idx]] += 1
        
#         return False

            
            