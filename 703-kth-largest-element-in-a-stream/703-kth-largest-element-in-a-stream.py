class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.heap, self.cap = nums[:k], k
        heapq.heapify(self.heap)
        for num in nums[k:]:
            heapq.heappushpop(self.heap, num)
                    
    def add(self, val: int) -> int:     
        if len(self.heap) < self.cap:
            heapq.heappush(self.heap, val)
        else: 
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
