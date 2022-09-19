class Solution:
    def leftNearestEle(self, heights: List[int]) -> List[int]:
        nearestLargest = []

        maxL = 0
        
        for val in heights:
            maxL = max(maxL, val)
            nearestLargest.append(maxL)
        
        return nearestLargest
    
    def trap(self, height: List[int]) -> int:
        leftLargest = self.leftNearestEle(height)
        rightLargest = list(reversed(self.leftNearestEle(reversed(height))))
        
        
        total = 0
        for idx, i in enumerate(height):
            total += min(leftLargest[idx], rightLargest[idx])  - i
        
        return total