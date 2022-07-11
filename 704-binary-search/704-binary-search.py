class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = start + ((end - start) // 2)
            
            ele = nums[mid]
            print(ele)
            
            if ele == target:
                return mid
            elif ele < target:
                # import pdb
                # pdb.set_trace()
                if nums[end] == target:
                    return end
                start = mid + 1
            else:
                if nums[start] == target:
                    return start
                end = mid - 1
        
        return -1