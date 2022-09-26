# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def __init__(self):
        self.result = -1
    
    def dfs(self, root, level):
        # base case
        if not root:
            self.result = max(self.result, level-1)
            return
        # logic
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.dfs(root, 1)
        return self.result

#         if not root:
#             return 0
        
#         bfsStack = deque()
        
#         bfsStack.append(root)
#         count = 0
#         while bfsStack:
#             count += 1
#             size = len(bfsStack)
            
#             for i in range(size):
#                 curr = bfsStack.popleft()
                
#                 if curr.left:
#                     bfsStack.append(curr.left)
#                 if curr.right:
#                     bfsStack.append(curr.right)

#         return count
        
        