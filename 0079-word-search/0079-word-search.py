class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def findword(index,r,c):
            if index==len(word): return True
            m,n = len(board), len(board[0])

            #Upper cell
            if r-1>=0 and c<n and (r-1,c) not in visited and board[r-1][c]==word[index]:
                visited.add((r-1,c))
                if findword(index+1,r-1,c):
                    return True
                visited.remove((r-1,c))
            
            #Below cell
            if r+1<m and c<n and (r+1,c) not in visited and board[r+1][c]==word[index]:
                visited.add((r+1,c))
                if findword(index+1,r+1,c):
                    return True
                visited.remove((r+1,c))

            #Left cell
            if r<m and c-1>=0 and (r,c-1) not in visited and board[r][c-1]==word[index]:
                visited.add((r,c-1))
                if findword(index+1,r,c-1):
                    return True
                visited.remove((r,c-1))
            
            #Right cell
            if r<m and c+1<n and (r,c+1) not in visited and board[r][c+1]==word[index]:
                visited.add((r,c+1))
                if findword(index+1,r,c+1):
                    return True
                visited.remove((r,c+1))

            return False

        
        m,n = len(board), len(board[0])
        if m*n < len(word): return False
        visited = set()
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    visited.add((i,j))
                    if findword(1,i,j): 
                        return True
                    visited.remove((i,j))
        
        return False