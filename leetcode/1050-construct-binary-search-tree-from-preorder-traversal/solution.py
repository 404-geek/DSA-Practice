# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        n = len(preorder)

        root = TreeNode(preorder[0])

        for i in range(1,n):

            val = preorder[i]
            curr = root

            while curr:
                if val < curr.val:
                    if not curr.left:
                        curr.left = TreeNode(val)
                        break
                    curr = curr.left
                
                if val > curr.val:
                    if not curr.right:
                        curr.right = TreeNode(val)
                        break
                    curr = curr.right

        return root

            
                    



                 
        
