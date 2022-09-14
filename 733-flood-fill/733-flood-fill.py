from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = {(1,0), (0, 1), (-1, 0), (0, -1)}
        visited = set()
        
        row = len(image)
        col = len(image[0])
        
        bfsStack = deque()
        
        setColor = image[sr][sc]
        bfsStack.append((sr, sc))
        
        while bfsStack:
            size = len(bfsStack)
            
            for i in range(size):
                curr = bfsStack.popleft()
                image[curr[0]][curr[1]] = color
                for d in directions:
                    nr = curr[0] + d[0]
                    nc = curr[1] + d[1]
                    
                    if 0 <= nr < row and 0 <= nc < col and image[nr][nc] == setColor and (nr, nc) not in visited:
                        bfsStack.append((nr, nc))
                        visited.add((nr, nc))
        
        return image
                    