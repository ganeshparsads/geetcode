class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) - 1
        res = letters[0]
        
        while start <= end:
            
            mid = start + (end - start) // 2
            
            ele = letters[mid]
            
            if ord(ele) == ord(target):
                start = mid + 1
            elif ord(ele) < ord(target):
                start = mid + 1
            else:
                end = mid - 1
                res = ele
        return res