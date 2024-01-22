class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        
        ans = [0, 1]
        
        for num in nums:
            if num in seen:
                ans[0] = num
            
            seen.add(num)
            
            while ans[1] in seen:
                ans[1]+=1
        
        return ans