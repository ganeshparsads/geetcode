# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def __init__(self):
        self.result = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        # result = []

        # if not root:
        #     return result

        # queue = deque()
        # queue.append(root)

        # while queue:
        #     size = len(queue)
        #     level = []
        #     for i in range(size):
        #         curr = queue.popleft()
        #         level.append(curr.val)
        #         if curr.left:
        #             queue.append(curr.left)
        #         if curr.right:
        #             queue.append(curr.right)
        #     result.append(level)
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, level):
        # base case
        if not root:
            return None
        # logic
        if len(self.result) == level:
            self.result.append([])
        self.result[level].append(root.val)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)

        
        
        