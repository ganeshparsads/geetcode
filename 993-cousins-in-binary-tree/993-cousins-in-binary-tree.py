# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.x_parent = None
        self.y_parent = None
        self.x_level = None
        self.y_level = None
    
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        self.dfs(root, None, x, y, 0)
        return self.x_parent != self.y_parent and self.x_level == self.y_level
    
    def dfs(self, root, parent, x, y, level):
        if root == None:
            return None
        
        if root.val == x:
            self.x_parent = parent
            self.x_level = level
        if root.val == y:
            self.y_parent = parent
            self.y_level = level
        
        self.dfs(root.left, root, x, y, level+1)
        self.dfs(root.right, root, x, y, level+1)