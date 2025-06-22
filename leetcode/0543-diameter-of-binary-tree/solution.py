# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def traverse(node):

            if not node:
                return 0
            
            left = traverse(node.left)
            right = traverse(node.right)

            self.res = max(self.res, left+right)


            return 1 + max(left, right)

        traverse(root)

        return self.res
