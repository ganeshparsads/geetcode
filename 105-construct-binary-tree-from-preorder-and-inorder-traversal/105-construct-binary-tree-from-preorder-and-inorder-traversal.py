# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.map = {}
        self.idx_preorder = 0
    
    def buildTree(self, preorder: List[int], inorder: List[int]):
        # null check
        # if not len(preorder):
        #     return None

        # # rootNode
        # rootVal = preorder[0]
        # rootNode = TreeNode(rootVal)

        # rootIdx = -1

        # # find the rootIndex from the preorder:
        # rootIdx = inorder.index(rootVal)

        # inLeft = list(inorder[0: rootIdx])
        # inRight = list(inorder[rootIdx+1: len(inorder)])
        # preLeft = list(preorder[1: len(inLeft)+1])
        # preRight = list(preorder[len(inLeft)+1: len(preorder)])



        # rootNode.left = self.buildTree(preLeft, inLeft)
        # rootNode.right = self.buildTree(preRight, inRight)

        # return rootNode

        # improved time complexity
        if not preorder:
            return None
        
        for idx, i in enumerate(inorder):
            self.map[i] = idx
        
        return self.helper(preorder, 0, len(preorder) - 1)
    
    def helper(self, preorder, start, end):
        if start > end:
            return None
        
        # logic
        
        root_val = preorder[self.idx_preorder]
        self.idx_preorder += 1
        
        rootIdx = self.map[root_val]
        
        rootNode = TreeNode(root_val)
        
        rootNode.left = self.helper(preorder, start, rootIdx - 1)
        
        rootNode.right = self.helper(preorder, rootIdx+1, end)
        
        return rootNode
