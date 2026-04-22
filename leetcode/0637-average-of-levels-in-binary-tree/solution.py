# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        q = deque([root])
        res = []
        
        while q:

            a = len(q)
            l_sum = 0
            for i in range(a):
                b = q.popleft()
                if b.left:
                    q.append(b.left)
                if b.right:
                    q.append(b.right)
                l_sum+=b.val

            res.append(float(l_sum / a))

        return res
            



