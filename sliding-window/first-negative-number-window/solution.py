import collections

class Solution:
    # prob: https://www.geeksforgeeks.org/first-negative-integer-every-window-size-k/
    def firstNegativeWindow(self, nums, k):
        start = 0
        end = 0
        windowArray = collections.deque()
        negativeArray = []

        length = len(nums)

        while (end < length):

            if nums[end] < 0:
                windowArray.append(nums[end])

            if (end - start + 1) != k:
                end += 1
            else:

                if not windowArray:
                    negativeArray.append(0)
                else:
                    negativeArray.append(windowArray[0])

                    if nums[start] == windowArray[0]:
                        windowArray.popleft()

                end += 1
                start += 1

        return negativeArray
