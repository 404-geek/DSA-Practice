# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ans = None
        cnt = 0

        def inorder(root):
            nonlocal ans, cnt

            if not root:
                return None

            if inorder(root.left):
                return

            cnt+=1

            if cnt == k:
                ans = root.val
                return True
            

            if inorder(root.right):
                return 


        inorder(root)

        return ans

        


