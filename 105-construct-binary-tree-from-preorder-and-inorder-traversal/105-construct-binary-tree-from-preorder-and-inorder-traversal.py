# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # null check
        if not len(preorder):
            return None

        # rootNode
        rootVal = preorder[0]
        rootNode = TreeNode(rootVal)
        
        rootIdx = -1
        
        # find the rootIndex from the preorder:
        rootIdx = inorder.index(rootVal)
        
        inLeft = list(inorder[0: rootIdx])
        inRight = list(inorder[rootIdx+1: len(inorder)])
        preLeft = list(preorder[1: rootIdx+1])
        preRight = list(preorder[len(inLeft)+1: len(preorder)])
        
        rootNode.left = self.buildTree(preLeft, inLeft)
        rootNode.right = self.buildTree(preRight, inRight)
        
        return rootNode

                      


        
        
        
        