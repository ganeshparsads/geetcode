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
        # count left and right at each level
        # sum of them is the answer
        # but in the reverse approach
        leftH = self.findHeight(root.left)
        
        rightH = self.findHeight(root.right)
        
        self.ans = max(self.ans, leftH+rightH)
        
        # while returning from the bottom level to top level
        # return the max of either one of the tree since we need to use deepest branch
        # addition 1 for that level
        return max(leftH, rightH) + 1
        