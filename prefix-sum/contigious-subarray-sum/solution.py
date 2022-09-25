from collections import defaultdict

class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        prefix_sum = [0 for i in range(len(nums))]
        
        hMap = defaultdict(int)
        hMap[0] += 1

        import pdb
        pdb.set_trace()
        
        for idx, i in enumerate(nums):
            if idx == 0:
                prefix_sum[idx] = i
            else:
                prefix_sum[idx] = prefix_sum[idx-1] + i
            
            if i % k != 0:
                new_sum = 10000000
                m = 0

                if prefix_sum[idx] % k == 0:
                    return True

                while new_sum > nums[0]:
                    new_sum = prefix_sum[idx] - m*k
                    if new_sum in hMap:
                        return True
                    m += 1

            hMap[prefix_sum[idx]] += 1
        
        return False
            
obj = Solution()

print(obj.checkSubarraySum([5, 0, 0, 0], 3))
