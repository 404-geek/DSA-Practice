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

        def lca(node):

            if not node:
                return None

            if node == p:
                return p
            
            if node == q:
                return q

            a = lca(node.left)
            b = lca(node.right)

            if a and b:
                return node

            return a or b

        return lca(root)


        