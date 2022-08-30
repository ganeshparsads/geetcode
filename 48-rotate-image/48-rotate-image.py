class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        
        currCol = n - 1
        
        result = [[matrix[j][i] for i in range(m)] for j in range(n)]
        
        print(result)
        
        for i in range(n):
            for j in range(m):
                matrix[j][currCol] = result[i][j]
            currCol -= 1

        # print(matrix)
