from heapq import heappush, heappop

class Solution:

    def binary_search(self, arr, x):
        start = 0
        end = len(arr) - 1

        if x in arr:
            i = arr.index(x)
            return i, i
        else:
            if x < arr[start]:
                return -1, -1
            if x > arr[end]:
                return len(arr), len(arr)
        # import pdb
        # pdb.set_trace()

        while start < end:
            mid = (start + end) // 2

            if mid == start:
                break

            if arr[mid] <= x:
                start = mid
            else:
                end = mid

        if abs(arr[mid-1]-x) < abs(arr[mid+1] - x):
            return mid-1, mid
        else:
            return mid, mid+1

    def findClosestElements(self, arr, k, x):
        # diff = list(map(lambda n: (-1*abs(n-x), n), arr))
        # maxHeap = []

        # for i in diff:
        #     print(i)
        #     if len(maxHeap) < k:
        #         heappush(maxHeap, i)
        #     else:
        #         if maxHeap[0][0] < i[0]:
        #             heappop(maxHeap)
        #             heappush(maxHeap, i)
        #         elif maxHeap[0][0] == i[0] and maxHeap[0][1] > i[1]:
        #             heappop(maxHeap)
        #             heappush(maxHeap, i[1])

        # result = []
        # for i in maxHeap:
        #     result.append(i[1])

        i, j = self.binary_search(arr, x)
        print(i, j)

        result = []

        if i == j:
            if i < 0:
                return arr[:k]
            if i == len(arr):
                return arr[k-1:]

            result.append(arr[i])
            i = i - 1
            j = j + 1

        while i >= 0 and j < len(arr) and len(result) < k:
            if abs(arr[i]-x) <= abs(x - arr[j]):
                result.append(arr[i])
                i -= 1
            else:
                result.append(arr[j])
                j += 1

        result = sorted(result)

        return result


        # return result


obj = Solution()

print(obj.findClosestElements([1,2,3,4,5], 4, 3))
