# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        i = 0
        n = len(preorder)

        def bounds(up):

            nonlocal i

            if i >= n or preorder[i] > up:
                return None

            root = TreeNode(preorder[i])
            i+=1
            root.left = bounds(root.val)
            root.right = bounds(up)

            return root

        return bounds(float("inf"))
