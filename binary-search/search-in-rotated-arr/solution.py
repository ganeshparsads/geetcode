class Solution:
    def findMin(self, nums, target):
        n = len(nums)
        start = 0
        end = n - 1

        while start <= end:
            mid = start + (end-start)//2

            ele = nums[mid]

            if ele == target:
                return mid

            if nums[start] <= ele:
                if nums[start] <= target and target < ele:
                    end = mid - 1
                else:
                    start = mid + 1

            else:
                if ele < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

obj = Solution()

print(obj.findMin([4,5,6,7,0,1,2], 1))
