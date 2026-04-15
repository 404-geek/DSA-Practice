# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def traverse(node):

            if node == None or node == p or node == q:
                return node

            a = traverse(node.left)
            b = traverse(node.right)

            if a and b:
                return node

            return a if a else b

        return traverse(root)

            
        
        
