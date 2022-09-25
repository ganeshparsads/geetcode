import heapq

minHeap = []
heapq.heapify(minHeap)

heapWithValues = [3,1,2]
heapq.heapify(heapWithValues)

print(heapWithValues)

maxHeap = [1,2,3]
maxHeap = [-x for x in maxHeap]
heapq.heapify(maxHeap)

heapq.heappush(heapWithValues, 5)

heapq.heappop(maxHeap)

print(maxHeap)

print(len(maxHeap))

# print(minHeap)
