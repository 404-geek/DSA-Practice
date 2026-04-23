# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        t_sum = 0

        if not root:
            return 0

        def summ(root):

            nonlocal t_sum

            if root.left:
                if root.left.left == None and root.left.right == None:
                    t_sum+=root.left.val
                else:
                    summ(root.left)
            
            if root.right:
                summ(root.right)

            return 0

        summ(root)

        return t_sum





