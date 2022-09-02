# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        bfsStack = deque()
        
        bfsStack.append(root)
        
        result = []

        while bfsStack:
            size = len(bfsStack)
            level_sum = 0
            for i in range(size):
                curr = bfsStack.popleft()
                level_sum += curr.val
                if curr.left:
                    bfsStack.append(curr.left)
                if curr.right:
                    bfsStack.append(curr.right)
            result.append(level_sum/size)
        
        return result