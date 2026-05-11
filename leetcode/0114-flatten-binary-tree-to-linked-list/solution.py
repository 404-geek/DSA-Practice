# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(root, prev):

            if not root:
                return prev

            prev = traverse(root.right, prev)
            prev = traverse(root.left, prev)

            root.right = prev
            root.left = None

            return root

        traverse(root, None)



        
        








        

        
         


        

