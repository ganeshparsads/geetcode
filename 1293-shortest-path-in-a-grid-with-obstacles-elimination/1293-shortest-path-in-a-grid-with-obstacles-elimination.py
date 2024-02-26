class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        def valid(row,col):
            return 0<=row<m and 0<=col<n
        seen=set()
        que=deque()
        seen.add((0,0,k))
        que.append((0,0,k,0))
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        while que:
            row,col,remain,steps=que.popleft()
            if row==m-1 and col==n-1:
                return steps
            for dx,dy in directions:
                new_row,new_col=row+dy,col+dx
                if valid(new_row,new_col):
                    if grid[new_row][new_col]==0:
                         if  (new_row,new_col,remain) not in seen:
                            seen.add((new_row,new_col,remain))
                            que.append((new_row,new_col,remain,steps+1))
                    elif remain and (new_row,new_col,remain-1) not in seen:
                          seen.add((new_row,new_col,remain-1))
                          que.append((new_row,new_col,remain-1,steps+1)) 
        return -1
