class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for x in range(n+1)] for x in range(m+1)]
        
        max_res = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = 1 + min(dp[i][j-1], min(dp[i-1][j], dp[i-1][j-1]))
                    max_res = max(max_res, dp[i][j])
        
        return max_res*max_res
        
#         global_max = 0 

#         for row in range(m):
#             for col in range(n):
#                 if matrix[row][col] == '1':
#                     local_max = 1
#                     global_max = max(global_max, local_max)
#                     k = 1
#                     flag = 0
#                     while row + k < m and col + k < n:
#                         for i in range(row, row + k + 1):
#                             if matrix[i][col + k] == "0":
#                                 flag = 1    
#                                 break
#                         for j in range(col, col + k): 
#                             if matrix[row + k][j] == "0":
#                                 flag = 1
#                                 break
#                         if flag == 1:
#                             break
                        
#                         k += 1
#                         global_max = max(global_max, k)
                        
#         return global_max * global_max