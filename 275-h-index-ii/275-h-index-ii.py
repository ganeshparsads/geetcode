class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        
        n = len(citations)
        
        for idx, val in enumerate(citations):
            diff = n - idx
            if val >= diff:
                return diff
        
        return 0
