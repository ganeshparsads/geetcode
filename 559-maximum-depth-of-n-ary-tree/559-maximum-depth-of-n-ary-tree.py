"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        
        if not root:
            return 0
        
        bfsStack = deque()
        
        bfsStack.append(root)
        count = 0
        while bfsStack:
            count += 1
            size = len(bfsStack)
            
            for i in range(size):
                curr = bfsStack.popleft()
                
                if curr.children:
                    for j in curr.children:
                        bfsStack.append(j)

        return count