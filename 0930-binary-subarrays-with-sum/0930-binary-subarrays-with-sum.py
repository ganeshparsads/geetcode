class Solution:
    def find_sum(self, nums, goal) -> int:
        if goal < 0:
            return 0
        
        l = 0
        r = 0
        n = len(nums)
        
        summ = 0
        cnt = 0

        
        while r < n:
            summ += nums[r]
            
            while summ > goal:
                summ = summ - nums[l]
                l += 1
            
            cnt += r - l + 1
            r = r + 1
        
        return cnt
    
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.find_sum(nums, goal) - self.find_sum(nums, goal-1)