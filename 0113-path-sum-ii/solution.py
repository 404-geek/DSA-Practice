# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:


        if not root:
            return []

        st = [(root, [root.val])]
        res = []

        while st:

            node, arr = st.pop()


            if not node.left and not node.right and sum(arr) == targetSum:
                res.append(arr)

            if node.left:
                st.append((node.left, arr + [node.left.val]))
            
            if node.right:
                st.append((node.right, arr + [node.right.val]))

        return res

