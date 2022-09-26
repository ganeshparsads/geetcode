# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
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
                
                if curr.left:
                    bfsStack.append(curr.left)
                if curr.right:
                    bfsStack.append(curr.right)

        return count
        
        