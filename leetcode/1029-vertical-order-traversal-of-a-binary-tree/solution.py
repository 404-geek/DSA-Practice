# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        map = defaultdict(list)

        q = Deque([(root,0, 0)])

        while q:
            
            a = len(q)

            for _ in range(a):

                no, row, co = q.popleft()

                map[co].append((row, no.val))

                if no.left:
                    q.append((no.left, row + 1, co - 1))

                if no.right:
                    q.append((no.right, row + 1, co + 1))

        res = []

        for col in sorted(map):
            val = map[col]

            val.sort()

            res.append([v for row, v in val])

        return res





