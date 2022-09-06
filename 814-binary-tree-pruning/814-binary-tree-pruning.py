# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        val = self.findHeight(root)
        
        if not val:
            root = None
        return root
    
    def findHeight(self, root: Optional[TreeNode]):
        # base case
        if not root:
            return 0
        # logic
        leftH = self.findHeight(root.left)
        rightH = self.findHeight(root.right)
        
        if leftH == 0:
            root.left = None
        if rightH == 0:
            root.right = None

        return max(leftH, rightH) + root.val