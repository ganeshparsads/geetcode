# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue: list[tuple[Optional[TreeNode], bool]] = deque([(root, False)])
        left_sum: int = 0

        while queue:
            node, is_left = queue.popleft()

            if not node:
                continue
            
            if not node.left and not node.right and is_left:
                left_sum += node.val
            
            queue.extend([(node.left, True), (node.right, False)])
        
        return left_sum