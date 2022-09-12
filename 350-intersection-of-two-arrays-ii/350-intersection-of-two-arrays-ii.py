from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            count = Counter(nums1)
            parse = nums2
        else:
            count = Counter(nums2)
            parse = nums1
        
        result = []
        for i in parse:
            if not count:
                break
            if i in count:
                result.append(i)
                count[i] -= 1
                if count[i] == 0:
                    count.pop(i, None)
        
        return result
