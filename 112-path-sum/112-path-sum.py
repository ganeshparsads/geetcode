# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.result = False
        if not root:
            return False
        self.helper(root, 0, targetSum)
        
        return self.result
        
    
    def helper(self, root, currSum, targetSum):
        # base case
        if not root:
            return True
        
        # if self.result:
        #     return True
        
        # logic
        currSum += root.val
        path.append(root.val)

        if not root.left and not root.right:
            if currSum == targetSum:
                # add the path to the result set
                print("reached here")
                self.result = True
                return self.result
            else:
                return False

        # left traversal
        result = self.helper(root.left, currSum, targetSum)

        # st.pop()

        # right traversal
        self.helper(root.right, currSum, targetSum)

        # backtracking
        path.pop()
