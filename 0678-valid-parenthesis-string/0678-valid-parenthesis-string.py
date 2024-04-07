class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        
        for ch in s:
            if ch != "*":
                d = 1 if ch == "(" else -1
                
                low += d
                high += d
            else:
                low -= 1
                high += 1
            
            if low < 0:
                low = 0

            if high < 0:
                return False
        
        return low == 0