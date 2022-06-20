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
    
    def isValidBSTIteration(self, root: Optional[TreeNode]) -> bool:
        self.inorder(root)
        return self.flag
    
        dq = collections.deque()
        dq.append(root)
        while root != null and dq:
            
            # inorder(push left)
            while root != null:
                dq.append(root)
                root = root.left
            
            root = dq.pop()
            
            if prev and prev.val >= root.val:
                return False
            prev = root
            root = root.right
        
        return True
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.minMaxHelper(root, -math.inf, math.inf)
        
    def minMaxHelper(self, root, min, max) -> bool:
        if not root:
            return True

        print(root.val, min, max)

        if root.val <= min or root.val >= max:
            print("Hi")
            return False


        left = self.minMaxHelper(root.left, min, root.val)
        right = self.minMaxHelper(root.right, root.val, max)

        return left and right