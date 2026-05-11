# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        r = preorder[0]

        root = TreeNode(r)

        idx = inorder.index(r)

        left_in = inorder[:idx]
        right_in = inorder[idx + 1:]

        left_size = len(left_in)

        left_pre = preorder[1: 1+ left_size]
        right_pre = preorder[1 + left_size :]

        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)

        return root



        


        
