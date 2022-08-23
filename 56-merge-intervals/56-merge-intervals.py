import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort based on the starting time
        intervals.sort()
        maxHeap = []
        
        for i in intervals:
            if not len(maxHeap):
                heapq.heappush(maxHeap, (-1*i[1], i[0]))
                continue

            top = maxHeap[0]
            top = -1*top[0]
            
            # merge step
            if top >= i[0] and top < i[1]:
                topInterval = heapq.heappop(maxHeap)
                newInterval = (-1*i[1], topInterval[1])
                heapq.heappush(maxHeap, newInterval)
            elif top < i[1]:
                newInterval = (-1*i[1], i[0])
                heapq.heappush(maxHeap, newInterval)

        result = []
        while maxHeap:
            topInterval = heapq.heappop(maxHeap)
            result.append([topInterval[1], -1*topInterval[0]])
        
        return result
