# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def reverse(x, y, is_odd):
            if x is None or y is None:
                return 
            if is_odd:
                x.val, y.val = y.val, x.val
            reverse(x.left, y.right, not is_odd)
            reverse(x.right, y.left, not is_odd)
        reverse(root.left, root.right, is_odd = True)
        return root
