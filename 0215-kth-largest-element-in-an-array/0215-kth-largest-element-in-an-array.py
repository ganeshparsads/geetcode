import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        
        h = []
        for idx, i in enumerate(nums):
            heapq.heappush(h, (-i, idx))
        
        result = -1
        for i in range(k):
            result = -1 * heapq.heappop(h)[0]
            
        return result