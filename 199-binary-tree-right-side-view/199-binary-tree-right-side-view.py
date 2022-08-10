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

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # BFS
        # result = []

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
        #     result.append(level[-1])

        # return result
        
        # DFS
        
        self.dfs(root, 0)
        
        # result = []
        
        # for i in self.traversal:
        #     result.append(i[-1])
        
        return self.result
        
    def dfs(self, root, level):
        # base
        if not root:
            return None        
        # logic
        print(root.val, level)
        
        # if len(self.result) > level:
        #     return None
        
        if len(self.result) == level:
            self.result.append(root.val)
        # else:
        #     self.result[level] = root.val
        self.dfs(root.right, level+1)
        self.dfs(root.left, level+1)


        