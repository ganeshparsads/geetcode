class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        
        for j in range(c):
            row = r-1
            for i in range(r):
                if i > row:
                    break
                matrix[i][j], matrix[row][j] = matrix[row][j], matrix[i][j]
                row -= 1
        
        for i in range(r):
            for j in range(i, c):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
        
                