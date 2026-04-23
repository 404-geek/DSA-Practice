# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        def traverse(a, b):
            

            if not a and not b:
                return True
            
            if not a or not b:
                return False
            
            if a.val != b.val:
                return False

            return traverse(a.left, b.right) and traverse(a.right, b.left)

        return traverse(root.left, root.right)

            
            
