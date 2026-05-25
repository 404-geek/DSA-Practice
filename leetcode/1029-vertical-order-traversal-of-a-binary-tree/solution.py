# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        nodes = []

        q = deque([(root,0, 0)])

        while q:

            node, p, l = q.popleft()

            nodes.append((p, l, node.val))

            if node.left:
                q.append((node.left, p - 1, l+1))

            if node.right:
                q.append((node.right, p + 1, l+1))

        nodes.sort()
        res = []
        prev_col = None
        for p, _, vals in nodes:

            if p != prev_col:
                res.append([])
            prev_col = p

            res[-1].append(vals)

        return res






        
