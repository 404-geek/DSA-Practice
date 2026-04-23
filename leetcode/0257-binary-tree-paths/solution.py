# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
        def traverse(root, path):

            path.append(root.val)

            if root.left == None and root.right == None:
                res.append("->".join(map(str, path)))
                path.pop()
                return

            if root.left:
                traverse(root.left, path)
            if root.right:
                traverse(root.right, path)

            path.pop()

        traverse(root, [])

        return res
