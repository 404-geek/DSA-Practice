# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traverse(root_p, root_q):

            if not root_p and not root_q:
                return True
            if not root_p or not root_q:
                return False
            if root_p.val != root_q.val:
                return False

            return traverse(root_p.left, root_q.left) and traverse(root_p.right, root_q.right)
            
        return traverse(p, q)
                
            

            


        
