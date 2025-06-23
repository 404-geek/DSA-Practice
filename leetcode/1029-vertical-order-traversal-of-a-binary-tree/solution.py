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

        map = defaultdict(list)

        q = deque([(root, root.val, 0, 0)])


        while q:

            for _ in range(len(q)):

                node, val, level, col = q.popleft()

                map[col].append((level,val))

                if node.left:

                    q.append((node.left, node.left.val, level+1, col-1))

                if node.right:

                    q.append((node.right, node.right.val, level+1, col+1))


        res = [
            [val for row, val in sorted(map[c], key=lambda x: (x[0], x[1]))]
            for c in sorted(map)
        ]
        return res

        return res



        
