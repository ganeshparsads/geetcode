import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        
        stones  = list(map(lambda n: -1 * n, stones))

        heapq.heapify(stones)
        while len(stones)!= 1:
            heapq.heappush(stones,-abs(heapq.heappop(stones) - heapq.heappop(stones)))
        return -stones[0]