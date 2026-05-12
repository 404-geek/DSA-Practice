# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)

        a = root

        while root:


            if val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return a
                root = root.right

            else:
                if root.left is None:
                    root.left = TreeNode(val)
                    return a
                root = root.left

        
