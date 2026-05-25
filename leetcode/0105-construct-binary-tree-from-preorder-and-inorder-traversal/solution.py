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

        root = preorder[0]
        node = TreeNode(root)

        ind = inorder.index(root)

        inord_l = inorder[:ind]
        inord_r = inorder[ind+1:]

        preord_l = preorder[1:ind+1]
        preord_r = preorder[1+ind:]

        node.left = self.buildTree(preord_l, inord_l)
        node.right = self.buildTree(preord_r, inord_r)

        return node
        
