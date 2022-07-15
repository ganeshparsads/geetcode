class Solution:
    def findMin(self, nums):
        n = len(nums)
        start = 0
        end = n - 1

        while start <= end:
            mid = start + (end-start)//2

            # max future can reach is (n - 1) if it's more than that
            # then roll it back to 0 by (n - 1 + 1)%n is 0
            future = (mid + 1) % n

            # min past can reach is 0 if it's less than that
            # then roll it back to (n - 1) by (0 + n - 1)%n is (n-1)
            past = (mid + n - 1) % n

            ele = nums[mid]

            if ele <= nums[future] and ele <= nums[past]:
                return ele
            elif nums[end] < ele:
                start = mid + 1
            else:
                end = mid - 1

obj = Solution()
print(obj.findMin([4,5,6,7,0,1,2]))
