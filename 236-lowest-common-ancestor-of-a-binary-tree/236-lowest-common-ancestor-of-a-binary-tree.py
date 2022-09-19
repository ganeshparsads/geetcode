from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.pPath = []
        self.qPath = []

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.helper(root, p, q, [root])
        for i in range(min(len(self.pPath), len(self.qPath))):
            if self.pPath[i].val != self.qPath[i].val:
                return self.pPath[i-1]
        
        if len(self.pPath) < len(self.qPath):
            return self.pPath[len(self.pPath) - 1]

        return self.qPath[len(self.qPath) - 1]
        
    
    def helper(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', path):
        # base
        if not root:
            return
        path.append(root)
        if root.val == p.val:
            self.pPath = list(path)
        if root.val == q.val:
            self.qPath = list(path)

        # logic
        self.helper(root.left, p, q, path)
        self.helper(root.right, p, q, path)

        # backtrack
        path.pop()

#         bfsStack = deque()
        
#         bfsStack.append((root, [root]))
        
#         pPath = []
        
#         qPath = []
        
#         while bfsStack:
#             size = len(bfsStack)
            
#             for i in range(size):
#                 curr, path = bfsStack.popleft()

#                 if curr.val == p.val:
#                     pPath = list(path)

#                 if curr.val == q.val:
#                     qPath = list(path)

#                 if curr.left:
#                     new_curr = curr.left
#                     new_path = list(path)
#                     new_path.append(curr.left)
#                     bfsStack.append((curr.left, list(new_path)))

#                 if curr.right:
#                     new_curr = curr.right
#                     new_path = list(path)
#                     new_path.append(curr.right)
#                     bfsStack.append((curr.right, list(new_path)))
        
#         for i in range(min(len(pPath), len(qPath))):
#             if pPath[i].val != qPath[i].val:
#                 return pPath[i-1]
        
#         if len(pPath) < len(qPath):
#             return pPath[len(pPath) - 1]

#         return qPath[len(qPath) - 1]
