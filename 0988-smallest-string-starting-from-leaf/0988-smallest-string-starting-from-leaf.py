class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        def dfs(node, path):
            if not node:
                return ""
            path = chr(node.val + ord('a')) + path
            if not node.left and not node.right:  # If leaf node
                return path
            left_path = dfs(node.left, path)
            right_path = dfs(node.right, path)
            if left_path and right_path:  # Return the lexicographically smallest path
                return min(left_path, right_path)
            elif left_path:  # If only left path exists
                return left_path
            else:  # If only right path exists
                return right_path

        return dfs(root, "")
