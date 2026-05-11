# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def leftHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        
        def rHeight(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        if not root:
            return 0

        l = leftHeight(root)
        r = rHeight(root)

        if l == r:
            return (2 ** (l)) - 1
        else:

            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        
