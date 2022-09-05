"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.result = []
    
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return self.result
        self.dfs(root, 0)
        # self.result.append([root.val])
        return self.result
    
    def dfs(self, root, level):
        if root == None:
            return
        else:
            if level == len(self.result):
                self.result.append([])
            self.result[level].append(root.val)
            for child in root.children:
                self.dfs(child, level+1)
