# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def isMirror(left, right):
            # Base case: both nodes are None
            if not left and not right:
                return True
            # If only one is None or values don't match, return False
            if not left or not right or left.val != right.val:
                return False
            
            # Recursive case: check if subtrees are mirrors
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

    
        return isMirror(root.left, root.right)
