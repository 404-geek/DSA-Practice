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

            a = max(0, find_sum(root.left))
            b = max(0, find_sum(root.right))

            su = max(su, root.val + a + b)

            return root.val + max(a, b)

        find_sum(root) 

        return su


        
