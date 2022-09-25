from collections import deque
import heapq

class Solution:
    def answerQueries(self, nums, queries):
        res = []
        
        nums  = sorted(nums)
        sorted_queries = sorted(queries)
        dq = deque(sorted_queries)
        
        minHeap = []
        # heapq.heappush(minHeap, (0, -1))

        for idx, val in enumerate(nums):
            if not minHeap:
                heapq.heappush(minHeap, (val, idx+1))
            else:
                heapq.heappush(minHeap, (minHeap[0][0] + val, idx+1))
        
        result = {}

        total = 0
        
        val = 0
        
        for i in sorted_queries:
            
            while minHeap and minHeap[0][0] <= i:
                key, val = heapq.heappop(minHeap)
            result[i] = val
        
        
        final = []
        for q in queries:
            final.append(result[q])
        
        return final


nums = [4,5,2,1]
quereis = [3,10,21]

obj = Solution()
print(obj.answerQueries(nums, quereis))
