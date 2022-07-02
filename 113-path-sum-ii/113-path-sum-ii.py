# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result = []
        if not root:
            return self.result
        
        self.helper(root, 0, [], targetSum)
        return self.result
    
    def helper(self, root, currSum, path, targetSum):
        # base case
        if not root:
            return
        
        # logic
        currSum += root.val
        path.append(root.val)
        
        if not root.left and not root.right:
            if currSum == targetSum:
                # add the path to the result set
                self.result.append(path)        
        
        # left traversal
        self.helper(root.left, currSum, list(path), targetSum)
        
        # st.pop()
        
        if root.right:
            self.helper(root.right, currSum, list(path), targetSum)
        