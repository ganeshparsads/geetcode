class Solution:
    def getMin(self, nums):
        min_num = float('inf')
        for i in nums:
            if i == 0:
                continue
            min_num = min(min_num, i)
        
        return min_num
    
    def minimumOperations(self, nums):
        n = len(nums)
        cnt = 0
        while sum(nums) != 0:
            cnt += 1
            min_num = self.getMin(nums)
            # print(min_num)
            for idx in range(len(nums)):
                if nums[idx] == 0:
                    continue

                nums[idx] -= min_num
        
        return cnt
