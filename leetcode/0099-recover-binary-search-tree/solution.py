# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        prev = None
        first = None
        middle = None
        last = None

        def traverse(root):

            nonlocal prev, first, middle, last

            if not root:
                return

            traverse(root.left)

            if prev and root.val < prev.val:
                if not first:
                    first = prev
                    middle = root
                else:
                    last = root

            prev = root

            traverse(root.right)

        traverse(root)

        if first and last:
            first.val, last.val = last.val, first.val
        else:
            first.val, middle.val = middle.val, first.val


            



        
