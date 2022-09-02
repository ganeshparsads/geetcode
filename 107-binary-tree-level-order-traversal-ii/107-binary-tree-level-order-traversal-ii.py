# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        bfsStack = deque()
        bfsStack.append(root)
        result = []
        while bfsStack:
            size = len(bfsStack)
            level = []
            for i in range(size):
                curr = bfsStack.popleft()
                level.append(curr.val)
                
                if curr.left:
                    bfsStack.append(curr.left)
                
                if curr.right:
                    bfsStack.append(curr.right)
            
            result.append(level)
        result.reverse()
        return result