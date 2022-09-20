# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        
        first = None
        second = None
        prev = None
        
        while root!= None or stack:

            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            if prev != None and prev.val > root.val:
                if not first:
                    first = prev
                    second = root
                else:
                    second = root
                
            
            prev = root
            root = root.right
        
        temp = first.val
        first.val = second.val
        second.val = temp

        