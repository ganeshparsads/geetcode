from collections import Counter

class Solution:
    def binaySearch(self, start, nums, target):
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start)//2
            
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                if start == mid or nums[mid-1] != nums[mid]:
                    return mid
                else:
                    end = mid - 1

        return -1
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        if len(nums1) < len(nums2):
            parse = nums1
            search = nums2
        else:
            parse = nums2
            search = nums1
        
        result = []
        start = 0
        for i in parse:
            mid = self.binaySearch(start, search, i)
            print(i, mid)
            if mid != -1:
                result.append(i)
                start = mid + 1

        return result
        
#         if len(nums1) < len(nums2):
#             count = Counter(nums1)
#             parse = nums2
#         else:
#             count = Counter(nums2)
#             parse = nums1
        
#         result = []
#         for i in parse:
#             if not count:
#                 break
#             if i in count:
#                 result.append(i)
#                 count[i] -= 1
#                 if count[i] == 0:
#                     count.pop(i, None)
        
        return result
