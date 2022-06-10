/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private static int ans = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        ans = 0;
        findHeight(root);
        return ans;
    }

    public int findHeight(TreeNode root) {
        if(root==null){
            return 0;
        }

        int leftTreeHeight = findHeight(root.left);
        int rightTreeHeight = findHeight(root.right);

        int diameter = leftTreeHeight + rightTreeHeight;

        ans = Math.max(ans, diameter);

        return Math.max(leftTreeHeight,rightTreeHeight) + 1;        
    }
}