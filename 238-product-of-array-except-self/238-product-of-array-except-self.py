class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        
        
        for idx, i in enumerate(nums):
            if idx == 0:
                continue
            res[idx] = res[idx-1]*nums[idx-1]

        print(res)

        rp = 1
        for idx in range((len(nums)-2), -1, -1):
            print(idx)
            rp *= nums[idx+1]
            res[idx] = res[idx]*rp
        
        return res
            