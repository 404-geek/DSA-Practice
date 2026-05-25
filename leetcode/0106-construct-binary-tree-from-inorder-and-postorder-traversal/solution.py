# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder or not postorder:
            return None

        root = postorder[-1]

        node = TreeNode(root)

        ind = inorder.index(root)
        inord_l = inorder[:ind]
        inord_r = inorder[ind+1:]

        l = len(postorder)

        postord_l = postorder[:ind]
        postord_r = postorder[ind:l-1]

        node.left = self.buildTree(inord_l, postord_l)
        node.right = self.buildTree(inord_r, postord_r)

        return node
