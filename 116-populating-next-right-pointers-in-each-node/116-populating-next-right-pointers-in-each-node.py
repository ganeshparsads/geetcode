"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        bfsStack = deque()
        
        bfsStack.append(root)
        
        while bfsStack:
            size = len(bfsStack)
            level = []
            print("size:", size)
            for i in range(size):
                curr = bfsStack.popleft()
                print("level: ", curr.val)
                level.append(curr)
                if curr.left:
                    bfsStack.append(curr.left)
                if curr.right:
                    bfsStack.append(curr.right)

            prev = None
            print(level)
            for idx, node in enumerate(level):
                if idx != 0:
                    prev.next = node
                prev = node

            prev.next = None

        return root