from collections import deque

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            if k < 10:
                return [k]
            else:
                return []
        
        digitCount = 0
        bfsStack = deque()
        
        for i in range(1, 10):
            bfsStack.append((i, i))

        digitCount = 1
        
        while bfsStack:
            size = len(bfsStack)
            
            for i in range(size):
                digit, currVal = bfsStack.popleft()
                
                for new_digit in range(0, 10):
                    if abs(new_digit-digit) == k:
                        bfsStack.append((new_digit, currVal*10+new_digit))

            digitCount += 1
            
            if digitCount == n:
                break
        
        result = []
        while bfsStack:
            result.append(bfsStack.popleft()[1])
        return list(result)