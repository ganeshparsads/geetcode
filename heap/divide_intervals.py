import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minHeap = []
        
        result = -1
        
        for i in intervals:
            heapq.heappush(minHeap, i[1])
            
            while minHeap and minHeap[0] <= i[0]:
                heapq.heappop(minHeap)

            result = max(result, len(minHeap))

        return result

