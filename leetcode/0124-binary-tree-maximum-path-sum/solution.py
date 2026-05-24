# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        su = float("-inf")

        def find_sum(root):

            nonlocal su

            if not root:
                return 0

            a = find_sum(root.left)
            b = find_sum(root.right)

            v = max(root.val, root.val + a, root.val + b)

            su = max(su, v, root.val + a + b)

            if v < 0:
                return 0

            return v

        find_sum(root)

        return su


        
