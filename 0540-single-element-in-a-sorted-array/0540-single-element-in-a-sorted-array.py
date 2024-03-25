class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, len(nums)-1


        while l <= r:
            mid  = l + (r-l)//2

            print(mid)
            if nums[mid] != nums[ (mid+1)%n ] and  nums[mid] != nums[(mid-1+n) % n]:
                return nums[mid]


            if mid %2 == 0:
                if nums[mid] == nums[mid-1]:
                    r = mid-1
                else :
                    l = mid +1
            else:
                if nums[mid] == nums[mid-1]:
                    l = mid +1
                else :
                    r = mid-1

        return nums[r]
        
        
        