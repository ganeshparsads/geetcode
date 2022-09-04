# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def solution(root, l, c):     #  l -> level number  and  c -> column number
            if root is None:
                return
            mapp[(c,l)].append(root.val)
            solution(root.left, l + 1, c - 1)
            solution(root.right, l + 1, c + 1)
            
        mapp = defaultdict(list)
        solution(root, 0, 0)
        res = []
        old = float("-inf")
        
        for k, v in sorted(mapp.items()):
            
            if k[0] != old:   # to check whenever a new index/vertical column starts
                res.append([])
                
            res[-1].extend(sorted(v))
            old = k[0]
        return res