class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        hashMap = {}
        
        for idx, digit in enumerate(digits):
            hashMap[digit] = idx
        
        for idx, digit in enumerate(digits):
            for d in range(9, 0, -1):
                d = str(d)
                if d in hashMap and hashMap[d] > idx:                 
                    if digit < d:
                        digits[idx], digits[hashMap[d]] = digits[hashMap[d]], digits[idx]
                        return int("".join(digits))
        
        
        return num
