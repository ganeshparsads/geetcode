class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = [0 for i in range(len(nums))]

        result = -1
        
        # prefix sum by making 0 to -1
        for idx, i in enumerate(nums):
            if idx == 0:
                if i == 0:
                    prefix_sum[idx] = -1
                else:
                    prefix_sum[idx] = 1
                continue
            if i == 1:
                prefix_sum[idx] = prefix_sum[idx-1] + 1
            else:
                prefix_sum[idx] = prefix_sum[idx-1] - 1
            
            if prefix_sum[idx] == 0:
                result = idx + 1
        
        hMap = {}
        
        # calculate
        for idx, i in enumerate(prefix_sum):
            if i not in hMap:
                hMap[i] = (idx+1, idx+1)
            else:
                start, end = hMap[i]
                hMap[i] = (start, idx+1)

        for key, val in hMap.items():
            start, end = val
            result = max(result, end - start)

        return result
        
        