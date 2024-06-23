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
    
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n  = len(nums)
        for i in range(n):
            if nums[i] % 2 != 0:
                nums[i] = 1
            else:
                nums[i] = 0
        
        print(nums)
            
        
        return self.find_sum(nums, k) - self.find_sum(nums, k-1)
        
        