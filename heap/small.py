from collections import Counter

class Solution:
    def mostFrequentEven(self, nums) -> int:
        count = Counter(nums)
        
        maxKey = -1
        maxFreq = -1
        
        for k, v in count.items():
            if k % 2 == 0:
                if maxFreq == v and maxKey > k:
                    maxKey = k
                
                if maxFreq < v:
                    maxKey = k
                    maxFreq = v
        
        return maxKey

obj = Solution()

print(obj.mostFrequentEven([8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]))
