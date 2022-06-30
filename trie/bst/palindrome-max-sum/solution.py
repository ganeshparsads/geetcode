class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        dq = collections.deque()
        currSum = [0]
        
        while root != None or dq:
            if not root:
                return 0

            while root != None:
                currSum.append(currSum[-1] + root)
                dq.push(root)
                root = root.left

            root = dq.pop()
            
            if root.left == None and root.right == None:
                lastSum = currSum.pop()
                if lastSum == targetSum:
                    return True
            root = root.right

        return False