# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            a = max(0, dfs(node.left))
            b = max(0, dfs(node.right))

            s = a + node.val + b

            max_sum = max(s, max_sum)

            return node.val + max(a, b)

        dfs(root)

        return max_sum


