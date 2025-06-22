# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        if not root:
            return []

        st = [(root, str(root.val))]
        res = []

        while st:

            node, path = st.pop()

            if not node.left and not node.right:

                res.append(path)

            if node.left:
                st.append((node.left, path+ "->" +str(node.left.val)))

            if node.right:
                st.append((node.right, path+ "->" +str(node.right.val)))

        
        return res


