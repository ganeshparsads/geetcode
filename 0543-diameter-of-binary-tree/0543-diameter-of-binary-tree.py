# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.findHeight(root)

        return self.ans
    
    def findHeight(self, root):
        # base
        if not root:
            return 0        
        
        # logic
        leftH = self.findHeight(root.left)
        
        rightH = self.findHeight(root.right)

        self.ans = max(self.ans, leftH+rightH)
        
        return max(leftH, rightH) + 1