class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        c_min = 1
        c_max = 1
        
        res = max(nums)
        
        for n in nums:
            # if n == 0:
            #     c_min = 1
            #     c_max = 1
            tmp = c_max*n
            c_max = max(tmp, c_min*n, n)
            c_min = min(tmp, c_min*n, n)
            
            print(c_max, c_min)
            res = max(res, c_max)
        
        return res
        
        
        