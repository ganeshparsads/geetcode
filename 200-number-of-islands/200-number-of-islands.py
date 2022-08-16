from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ones = set()
        
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ones.add((i, j))
        
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        if not len(ones):
            return 0

        bfsStack = deque()
        curr = ones.pop()
        bfsStack.append(curr)

        count = 1
        
        while bfsStack:
            curr = bfsStack.pop()
            for dirt in directions:
                nr = curr[0] + dirt[0]
                nc = curr[1] + dirt[1]

                if nr >= 0 and nc >= 0 and nr < n and nc < m and grid[nr][nc] == "1" and (nr, nc) in ones:
                    ones.remove((nr, nc))
                    bfsStack.append((nr, nc))

            if not bfsStack and ones:
                bfsStack.append(ones.pop())
                count += 1

        return count
