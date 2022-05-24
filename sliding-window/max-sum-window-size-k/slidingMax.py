import collections

class Solution:
    def maxSlidingWindow(self, nums, k):
        start = 0
        end = 0
        maxArray = []
        prevMax = 
        windowArray = collections.deque()

        while (end < len(nums)):
            windowArray.append(nums[end])
            if (end - start + 1) < k:
                end += 1
            else:
                maxArray.append(max(windowArray))
                windowArray.popleft()
                end += 1
                start += 1
        return maxArray


# def maxSlidingWindow(self, nums, k):
#     d = collections.deque()
#     out = []
#     for i, n in enumerate(nums):
#         while d and nums[d[-1]] < n:
#             d.pop()
#         d += i,
#         if d[0] == i - k:
#             d.popleft()
#         if i >= k - 1:
#             out += nums[d[0]],
#     return out