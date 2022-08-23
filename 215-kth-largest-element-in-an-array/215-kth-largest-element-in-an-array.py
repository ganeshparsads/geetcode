import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        
        for idx, val in enumerate(nums):            
            if len(minHeap) < k:
                heapq.heappush(minHeap, val)
            else:
                if minHeap[0] <= val:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, val)

        return minHeap[0]
