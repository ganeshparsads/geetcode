class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        abs_array = []
        
        if k >= len(arr):
            return arr
        
        for i in arr:
            abs_array.append(abs(i - x))

        i = 0
        j = len(arr) - 1
        
        while (abs(i-j) + 1) > k:
            if abs_array[j] >= abs_array[i]:
                j -= 1
            else:
                i += 1
            
        result = []
        
        while i <= j:
            result.append(arr[i])
            i += 1
        
        return result