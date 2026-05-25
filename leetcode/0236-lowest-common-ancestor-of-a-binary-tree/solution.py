# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return None

        def find_lca(root, p, q):

            if not root:
                return None
            
            if root == p or root == q:
                return root

            a = find_lca(root.left, p, q)
            b = find_lca(root.right, p, q)

            if a and b:
                return root

            if a:
                return a
            
            if b:
                return b

            return None

        return find_lca(root, p, q)





