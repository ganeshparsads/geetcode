# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.helper(root)
        return self.result
    
    def helper(self, root):
        # base
        if not root:
            return
        
        # logic
        self.helper(root.left)
        self.helper(root.right)
        self.result.append(root.val)