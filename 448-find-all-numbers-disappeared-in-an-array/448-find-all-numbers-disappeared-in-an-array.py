class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = [False]*(len(nums)+1)
        
        final = []
        
        for i in nums:
            res[i] = True
        
        for idx, val in enumerate(res):
            if idx == 0:
                continue

            if not val:
                final.append(idx)

        return final