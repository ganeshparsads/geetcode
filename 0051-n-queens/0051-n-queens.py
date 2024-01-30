class Solution:
    def __init__(self):
        self.result = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[False for i in range(n)] for j in range(n)]
        self.backTrack(0, board, n)
        return self.result
        
    
    def isSafe(self, r, c, board, n):
        # up columns
        for i in range(r):
            if board[i][c]:
                return False

        i = r
        j = c
        
        # left diagonal
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1
        
        i = r
        j = c
        
        # right diagonal
        while i >= 0 and j < n:
            if board[i][j]:
                return False
            i -= 1
            j += 1

        return True
    
    def backTrack(self, row, board, n):
        # base
        if row == n:
            partial_result = []
            for i in range(n):
                queens = []
                for j in range(n):
                    if board[i][j]:
                        queens.append("Q")
                    else:
                        queens.append(".")
                
                partial_result.append("".join(queens))
            
            self.result.append(partial_result)
        
        # logic
        for col in range(n):
            if self.isSafe(row, col, board, n):
                board[row][col] = True
                self.backTrack(row+1, board, n)
                board[row][col] = False
