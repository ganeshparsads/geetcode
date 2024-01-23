# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        bfsq, mapper = deque(), {}
        bfsq.append((root, [], 0))
        while bfsq : 
            node, lca, level = bfsq.popleft()

            if node.val not in mapper : 
                mapper[node.val] = []

            new_lca = lca + [(node.val, level)]
            mapper[node.val] += new_lca 

            if node.right : 
                bfsq.append((node.right, new_lca, level+1))
            if node.left :
                bfsq.append((node.left, new_lca, level+1))

        max_level, min_lca = -1, -1
        lca_p, lca_q = set(mapper[p.val]), set(mapper[q.val])
        if len(lca_p) < len(lca_q) :
            min_dist, long_dist = lca_p, lca_q
        else : 
            min_dist, long_dist = lca_q, lca_p
 
        for node, level in min_dist : 
            if (node, level) in long_dist :
                if level > max_level :
                    max_level = level 
                    min_lca = node 

        return TreeNode(min_lca)
