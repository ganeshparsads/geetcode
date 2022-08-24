class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n > 1:
            n = n/3
            
            if n != int(n):
                return False
        
        return True