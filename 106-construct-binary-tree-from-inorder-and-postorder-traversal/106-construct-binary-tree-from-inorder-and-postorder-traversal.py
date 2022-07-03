# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # base case
        if not len(postorder):
            return None
        
        # logic:
        
        # get rootNode
        # from postOrder we will come to know the root node
        rootVal = postorder[-1]
        rootNode = TreeNode(rootVal)
        
        # find rootIndex
        rootIdx = inorder.index(rootVal)
        
        # inleft and inright
        inleft = list(inorder[0:rootIdx])
        inright = list(inorder[rootIdx+1:len(inorder)])
        
        # postLeft and postright
        postleft = list(postorder[0:len(inleft)])
        postright = list(postorder[len(inleft):len(postorder)-1])
        
        # print("inLeft: ", inleft)
        # print("inRight: ", inright)
        # print("postLeft: ", postleft)
        # print("postRight: ", postright)

        rootNode.left = self.buildTree(inleft, postleft)
        rootNode.right = self.buildTree(inright, postright)

        return rootNode
        