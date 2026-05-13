# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def traverse(root):
            nonlocal ans

            if not root:
                return True, float("inf"), float("-inf"), 0

            l_bst, l_min, l_max, l_sum = traverse(root.left)
            r_bst, r_min, r_max, r_sum = traverse(root.right)

            if l_bst and r_bst and l_max < root.val < r_min:
                curr_sum = l_sum + r_sum + root.val
                ans = max(ans, curr_sum)

                return True, min(l_min, root.val), max(r_max, root.val), curr_sum

            return False, 0, 0, 0

        traverse(root)
        return ans


            



        
