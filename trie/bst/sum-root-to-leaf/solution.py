# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    prev = None
    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)

        if self.prev:
            print(self.prev, root)

        prev = root

        self.inorder(root.right)
    
    def sumNumbers(self, root):
        
        