from heapq import heappush, heappop


class Solution:
    def findClosestElements(self, arr, k, x):
        diff = list(map(lambda n: (-1*abs(n-x), n), arr))
        maxHeap = []
        
        for i in diff:
            # print(i)
            if len(maxHeap) < k:
                heappush(maxHeap, i)
            else:
                if maxHeap[0][0] < i[0]:
                    heappop(maxHeap)
                    heappush(maxHeap, i)
                elif maxHeap[0][0] == i[0] and maxHeap[0][1] > i[1]:
                    heappop(maxHeap)
                    heappush(maxHeap, i[1])

        result = []
        for i in maxHeap:
            result.append(i[1])
        result = sorted(result)
        return result