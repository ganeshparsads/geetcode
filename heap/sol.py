from collections import deque

class Solution:
    def numIslands(self, grid, maxlen):
        def search_island(n):
            q=deque()
            q.append((0,0,1))
            direction=[(0,1),(0,-1),(1,0),(-1,0)]

            while q:
                temp_r,temp_c,length=q.popleft()

                if temp_r == n-1 and temp_c == n-1:
                    return True

                for dr,dc in direction:
                    row=temp_r+dr
                    col=temp_c+dc
                    #r,c=row_size, col_size of grid that is mention below
                    if -1<row<r and -1<col<c and ((row,col) not in visit) and grid[row][col]=='.' and maxlen >= (length + 1):
                        visit.add((row,col))
                        q.append((row,col,length+1))
            return False

        if not grid:
            return False
        r,c=len(grid),len(grid[0])
        visit=set()
        island=0

        return search_island(len(grid))


maze = ['..$$', '$.$$', '$...']

result = []

for i in maze:
    result.append(list(i))

obj = Solution()

print(obj.numIslands(result, 6))
