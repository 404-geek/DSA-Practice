# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        to_delete = set(to_delete)

        res = []

        def dfs(root, is_root):

            if not root:
                return None

            if root.val in to_delete:

                dfs(root.left, True)
                dfs(root.right, True)

                return None
            
            if is_root:
                res.append(root)

            root.left = dfs(root.left, False)
            root.right = dfs(root.right, False)

            return root

        
        dfs(root, True)

        return res
        
