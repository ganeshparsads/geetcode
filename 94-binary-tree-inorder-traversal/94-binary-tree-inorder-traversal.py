# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # morris implementation
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        curr = root

        while curr != None:
            # find the last element
            if curr.left == None:
                result.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right != None and pre.right != curr:
                    pre = pre.right
                
                if pre.right == None:
                    # create root back when coming from up to down
                    pre.right = curr

                    # move forward or move down
                    curr = curr.left
                else:
                    # print(curr.val)
                    result.append(curr.val)
                    print(pre.val, curr.val, curr.right, result)
                    pre.right = None
                    curr = curr.right
        return result
    
    # stack implementation
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            result.append(root.val)
            root = root.right
        
        return result
    # morris implementation
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        curr = root
        
        while curr != None:
            # print(curr.val)
            if curr.left == None:
                # print(curr.val)
                result.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right != None and pre.right != curr:
                    pre = pre.right

                if pre.right == None:
                    # create root back when coming from up to down
                    pre.right = curr

                    # move forward or move down
                    curr = curr.left
                else:
                    # print(curr.val)
                    result.append(curr.val)
                    print(pre.val, curr.val, curr.right, result)
                    pre.right = None
                    curr = curr.right
        
        return result