# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        bfs = deque()
        
        result = []
        
        bfs.append(root)
        
        while bfs:
            curr = bfs.popleft()

            if low <= curr.val <= high:
                result.append(curr.val)
            
            if low < curr.val and curr.left:
                bfs.append(curr.left)
            if high > curr.val and curr.right:
                bfs.append(curr.right)
            
        
        return sum(result)
