class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # Calculate total sum of entire array
        tsum = 0
        for n in nums:
            tsum += n
            
        # Target sum for sliding window. We search for sliding window sum = targetSum
        targetSum = tsum - x
        # Sliding window start and end
        i = 0
        j = len(nums) - 1
        # Best length var
        bestLength = 100001
        
        # Create the first sliding window
        while tsum > targetSum:
            try:
                tsum -= nums[j]
                j -= 1
            except:
                return -1
        
        # Move the sliding window until the start index reaches the end of the array
        while i < len(nums):
            # If the sliding window becomes smaller than [], move the right index
            if j < i - 1:
                j += 1
                tsum += nums[j]
                continue
                
                
            if tsum > targetSum:
                # If the current sum is too big, move the left index
                tsum -= nums[i]
                i += 1
            elif tsum == targetSum:
                # If the current sum is the target sum, update bestLength and move left index
                bestLength = min(bestLength, i + len(nums) - j - 1)
                tsum -= nums[i]
                i += 1
            else:
                # If the current sum is too small, move the right index
                j += 1
                try:
                    tsum += nums[j]
                except:
                    break
            
        # Return the bestLength if it exists (if it was ever updated)
        return -1 if bestLength == 100001 else bestLength