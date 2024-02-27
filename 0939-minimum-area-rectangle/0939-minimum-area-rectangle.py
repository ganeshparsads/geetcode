class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_size = float('inf')
        visited = set()
        
        for x1, y1 in points:
            for x2, y2 in visited:
                if (x1, y2) in visited and (x2, y1) in visited:
                    size = abs(x2-x1) * abs(y2-y1)
                    min_size = min(size, min_size)
            
            visited.add((x1, y1))
        
        if min_size == float('inf'):
            return 0

        return min_size