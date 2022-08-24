class Solution:
    def __init__(self):
        self.result = []
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        # if n < 4:
        #     return self.result
        
        board = [[False for i in range(n)] for j in range(n)]
        
        self.backTrack(board, 0, n)
        
        return self.result
    
    def backTrack(self, board, row, n):
        # base
        if row == n:
            li = []
            for i in range(n):
                col_string = ""
                for j in range(n):
                    if board[i][j]:
                        col_string += "Q"
                    else:
                        col_string += "."
                li.append(col_string)

            self.result.append(li)
            return

        # logic
        for i in range(n):
            if self.isSafe(board, row, i, n):
                # action
                board[row][i] = True
                
                # recurse
                self.backTrack(board, row+1, n)

                # backTrack
                board[row][i] = False

    def isSafe(self, board, r, c, n):
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
