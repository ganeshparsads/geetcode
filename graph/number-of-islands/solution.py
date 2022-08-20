from collections import deque

class Solution:
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        count = 0

        import pdb
        pdb.set_trace()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfsStack = deque((i, j))
                    count += 1
                    while bfsStack:
                        curr = bfsStack.pop()
                        grid[curr[0]][curr[1]] = "0"
                        for dirt in directions:
                            nr = curr[0] + dirt[0]
                            nc = curr[1] + dirt[1]

                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "1":
                                bfsStack.append((nr, nc))

        return count

obj = Solution()

ip = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

print(obj.numIslands(ip))
