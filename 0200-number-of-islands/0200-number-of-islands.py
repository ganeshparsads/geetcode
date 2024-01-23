from collections import deque

class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])

        ones = set()
        visited = set()
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ones.add((i,j))

        cnt = 0
        bfs = deque()        
        
        if ones:
            r,c = ones.pop()
            bfs.append((r,c))
            cnt += 1

        while ones:
            r,c = bfs.popleft()
            
            for d in dirs:
                new_r = r + d[0]
                new_c = c + d[1]

                if (-1 >= new_r or new_r >= m) or (-1 >= new_c or new_c>= n):
                    continue

                if grid[new_r][new_c] == "1" and (new_r, new_c) not in visited:
                    visited.add((new_r,new_c))
                    if (new_r, new_c) in ones:
                        ones.remove((new_r, new_c))
                    bfs.append((new_r, new_c))

            if not bfs and ones:
                bfs.append(ones.pop())
                cnt += 1
        
        return cnt
