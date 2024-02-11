class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        parse = []
        
        if len(nums1) <= len(nums2):
            hash_map = dict(Counter(nums1))
            parse = nums2
        else:
            hash_map = dict(Counter(nums2))
            parse = nums1
        
        result = []

        for i in parse:
            if i in hash_map and hash_map[i]:
                result.append(i)
                hash_map[i] -= 1

        return result
