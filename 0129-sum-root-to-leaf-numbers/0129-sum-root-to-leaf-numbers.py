# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        bfs = deque()
        bfs.append((root, 0))

        result = 0

        while bfs:
            size = len(bfs)
            for i in range(size):
                curr, root_val = bfs.popleft()

                curr_val = (root_val * 10 + curr.val)

                if not curr.left and not curr.right:
                    result += curr_val
                
                if curr.left:
                    bfs.append((curr.left, curr_val))
                
                if curr.right:
                    bfs.append((curr.right, curr_val))
        
        return result
