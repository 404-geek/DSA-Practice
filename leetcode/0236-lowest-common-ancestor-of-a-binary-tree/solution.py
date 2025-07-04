# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def LCA(node):

            if node == None:
                return None
            elif node == p or node == q:
                return node

            node1 = LCA(node.left)
            node2 = LCA(node.right)

            if node1 and node2:
                return node

            return node1 or node2


        return LCA(root)



