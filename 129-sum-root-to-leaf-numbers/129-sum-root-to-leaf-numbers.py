# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0

    def inorder(self, root, currSum):
        if not root:
            return 0

        leftSum = self.inorder(root.left, currSum*10 + root.val)

        if not root.left  and not root.right:
            self.result += currSum*10 + root.val
        
        rightSum = self.inorder(root.right, currSum*10 + root.val)
        
        return leftSum + rightSum

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.inorder(root, 0)
        return self.result