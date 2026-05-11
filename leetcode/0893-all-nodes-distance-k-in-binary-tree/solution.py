# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        if not root:
            return []

        map = {}
        q = deque([(root)])

        while q:

            for _ in range(len(q)):

                a = q.popleft()

                if a.left:
                    q.append(a.left)
                    map[a.left] = a
                if a.right:
                    q.append(a.right)
                    map[a.right] = a

        q.append((target, 0))
        vis = {target}

        res = []

        def move(q):

            while q:

                n, dis = q.popleft()

                if dis == k:
                    res.append(n.val)
                    continue

                if n in map and map[n] not in vis:
                    q.append((map[n], dis + 1))
                    vis.add(map[n])

                if n.left and n.left not in vis:
                    q.append((n.left, dis + 1))
                    vis.add(n.left)

                if n.right and n.right not in vis:
                    q.append((n.right, dis + 1))
                    vis.add(n.right)

        move(q)

        return res
                    

                

        



