class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        
        res = [0]*(m*n)
        
        i = 0
        j = 0
        di = 1
        idx = 0
        
        while (idx < m*n):
            res[idx] = mat[i][j]
            idx += 1
            
            if di == 1:
                if j == n-1:
                    i += 1
                    di = -1
                elif i == 0:
                    j += 1
                    di = -1
                else:
                    i -= 1
                    j += 1
            else:
                if i == m-1:
                    j += 1
                    di = 1
                elif j == 0:
                    i += 1
                    di = 1
                else:
                    i += 1
                    j -= 1

        return res
                    
                
                
            
        
        