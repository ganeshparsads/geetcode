from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = [0 for i in range(len(nums))]
        
        hMap = defaultdict(int)
        hMap[0] = 1
        count = 0

        for idx, i in enumerate(nums):
            if idx == 0:
                prefix_sum[idx] = i
            else:
                prefix_sum[idx] = prefix_sum[idx-1] + i
            
            diff = prefix_sum[idx] - k

            if diff in hMap:
                count += hMap[diff]

            hMap[prefix_sum[idx]] += 1
        
        return count

obj = Solution()

print(obj.subarraySum([1,1,1], 2))
