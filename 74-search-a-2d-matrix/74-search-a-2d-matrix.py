class Solution:
    def decodeIndex(self, mid: int, row_len: int):
        return mid//row_len, mid%row_len
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) * len(matrix[0]) - 1
        
        while start <= end:
            mid = start + (end - start)//2
            
            i, j = self.decodeIndex(mid, len(matrix[0]))
            print(i, j)
            ele = matrix[i][j]
            
            if ele == target:
                return True
            elif ele < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return False
