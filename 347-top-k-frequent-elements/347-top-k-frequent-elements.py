import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], threshold: int) -> List[int]:
#         freq = {}
#         for i in nums:
#             if i not in freq:
#                 freq[i] = 0
#             freq[i] += 1
        
#         minHeap = []
        
#         for key, value in freq.items():
#             if len(minHeap) < k:
#                 heapq.heappush(minHeap, (value, key))
#             else:
#                 if minHeap[0][0] < value:
#                     heapq.heappop(minHeap)
#                     heapq.heappush(minHeap, (value, key))
        
#         result  = []
#         for each in minHeap:
#             result.append(each[1])
        
#         return result
        # bucket sort way
        count = Counter(nums)
        
        freq = [[] for i in range(len(nums)+1)]
        
        for key, val in count.items():
            freq[val].append(key)
        
        result = []
        for j in range(len(nums), -1, -1):
            for k in freq[j]:
                result.append(k)
                if len(result) == threshold:
                    print("hi", result)
                    return result