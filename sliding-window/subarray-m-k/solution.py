import collections

class Solution:
    def subarraySum(self, nums, k):
        start = 0
        end = 0
        
        possibleArr = []
        
        maxIndices = collections.deque()
        
        n = len(nums)

        wSum = 0

        maxWindowSize = 0

        while end < n:

            wSum += nums[end]
            maxIndices.append(end)

            if wSum == k:
                windowSize = len(maxIndices)
                if maxWindowSize < windowSize:
                    maxWindowSize = windowSize

                maxIndices.popleft()
                wSum -= nums[start]
                start += 1
                end += 1
            else:
                end += 1

        print("Window length: ", maxWindowSize)
