# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        map = {}

        q = deque([root])

        while q:

            node = q.popleft()

            if node.left:
                map[node.left] = node
                q.append(node.left)
            
            if node.right:
                map[node.right] = node
                q.append(node.right)

        res = []
        vis = set([target])
        q.append((0,target))
        d = 0

        while q:

            d, node = q.popleft()

            if d == k:
                res.append(node.val)
                continue

            for nei in (node.left, node.right, map.get(node)):
                if nei and nei not in vis:
                    vis.add(nei)
                    q.append((d+1, nei))

        return res
            
            



        

            

        
