# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    flag = True
    prev = None
    
    def inorder(self, root):
        if root == None:
            return;
        
        self.inorder(root.left)
        
        if self.prev and self.prev.val >= root.val:
            self.flag = False
            return
        
        self.prev = root
        
        if self.flag:
            self.inorder(root.right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder(root)
        return self.flag