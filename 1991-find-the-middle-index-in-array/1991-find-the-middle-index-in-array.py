class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        prefix_sum = [0 for i in range(n)]
        suffix_sum = [0 for i in range(n)]
        
        for idx in range(n):
            if idx == 0:
                continue
            prefix_sum[idx] = prefix_sum[idx-1] + nums[idx-1]
            suffix_sum[n-idx-1] = suffix_sum[n-idx] + nums[n-idx]
        
        for i in range(n):
            if prefix_sum[i] == suffix_sum[i]:
                return i
        
        return -1