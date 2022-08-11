# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def validArray(self, li):
        i = 0
        j = len(li) - 1
        print(li)
        while i < j:
            if li[i] != li[j]:
                return False
            i += 1
            j -= 1
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        bfsStack = deque()
        bfsStack.append(root)
        
        while bfsStack:
            size = len(bfsStack)
            li = []
            
            for i in range(size):
                curr = bfsStack.popleft()
                if not curr:
                    li.append(None)
                else:
                    li.append(curr.val)
                if curr:
                    bfsStack.append(curr.left)
                    bfsStack.append(curr.right)

            if not self.validArray(li):
                return False

        return True
                    
            