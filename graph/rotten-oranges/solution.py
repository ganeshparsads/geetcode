from collections import deque

class Solution:
    def orangesRotting(self, grid):
        fresh = 0
        
        qStack = deque()
        
        dirs = [[-1, 0], [0, -1], [1,0], [0,1]]
        m = len(grid)
        n = len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    qStack.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if not fresh:
            return 0
        
        time = 0
        
        # import pdb
        # pdb.set_trace()

        while qStack:
            size = len(qStack)
            print(qStack)
            for i in range(size):
                curr = qStack.popleft()

                for di in dirs:
                    nr = curr[0] + di[0]
                    nc = curr[1] + di[1]
                    # print(nr, nc, grid[nr][nc])
                    if nr >= 0 and nc >= 0 and nr < m and nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        qStack.append((nr, nc))
                        fresh = fresh - 1
            time += 1
        
        if fresh:
            print(fresh)
            return -1
        else:
            return time - 1

obj = Solution()

print(obj.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
