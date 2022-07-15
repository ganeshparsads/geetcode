class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = start + ((end - start) // 2)
            
            ele = nums[mid]
            
            if ele == target:
                return mid
            elif ele < target:
                print("here")
                if nums[end] == target:
                    return end
                start = mid + 1
            else:
                print("fhere")
                if nums[start] == target:
                    return start
                end = mid - 1
        
        return -1

obj = Solution()

print(obj.search([1,3], 3))
