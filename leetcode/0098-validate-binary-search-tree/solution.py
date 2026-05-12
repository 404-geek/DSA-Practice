# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        def valid_BST(root, low, high):

            if not root:
                return True

            if not low < root.val < high:
                return False

            a = valid_BST(root.left, low, root.val)
            b = valid_BST(root.right, root.val, high)

            return a and b

        return valid_BST(root, float("-inf"), float("inf"))
