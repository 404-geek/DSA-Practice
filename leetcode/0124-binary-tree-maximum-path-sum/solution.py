# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxi = root.val
        
        def trav(root):

            nonlocal maxi

            if not root:
                return 0

            a = max(0,trav(root.left))
            b = max(0,trav(root.right))

            maxi = max(maxi, root.val + b + a)

            return root.val + max(a, b )

        trav(root)

        return maxi

