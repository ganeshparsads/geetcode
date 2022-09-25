from collections import deque

class Solution(object):
    def hasPath(self, maze, start, destination, maxlen):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # parameter, visited = [start], set()
        parameter = deque()

        bfsStack = deque()
        bfsStack.append(start, 1)
        result = []
        while bfsStack:
            size = len(bfsStack)
            level = []
            for i in range(size):
                curr = bfsStack.popleft()
                level.append(curr)
                
                if curr.left:
                    bfsStack.append(curr.left)
                
                if curr.right:
                    bfsStack.append(curr.right)
            if zigZag:
                level.reverse()
                zigZag = False
            else:
                zigZag = True
            
            result.append(level)
        return result
        return False

maze = ['..$$', '$.$$', '$...']

result = []

for i in maze:
    result.append(list(i))

obj = Solution()

print(obj.hasPath(result, [0, 0], [2, 2]))
