class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        major = 0
        
        for i in nums:
            if cnt == 0:
                major = i
            
            if i == major:
                cnt += 1
            else:
                cnt = cnt - 1

        return major
            