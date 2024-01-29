class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            x = 1/x
            n = -n
            return self.myPow(x,n)
        else:
            mid = n//2
            result = self.myPow(x,mid)
            finalresult = result * result
            if n % 2 == 0:
                return finalresult
                
            else:
                return x * finalresult