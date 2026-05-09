# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        if not root:return []

        if root.left:
            r = self.inorderTraversal(root.left)
            res += r

        res.append(root.val)

        if root.right:
            g = self.inorderTraversal(root.right)
            res+=g

        return res

        
