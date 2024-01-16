class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0    
        
        nums = set(nums)
        final = 1
        
        for i in nums:
            seq = []
            if i-1 not in nums:
                num = i

                while num in nums:
                    seq.append(i)                    
                    num += 1
            
            final = max(len(seq), final)
        
        return final