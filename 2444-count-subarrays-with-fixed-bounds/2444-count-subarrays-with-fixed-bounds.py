class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        bad_idx = left_idx = right_idx = -1
        
        for idx, val in enumerate(nums):
            if not minK <= val <= maxK:
                bad_idx = idx
            
            if minK == val:
                left_idx = idx
            if maxK == val:
                right_idx = idx
            
            res += max(0, min(left_idx, right_idx) - bad_idx)
        
        return res
