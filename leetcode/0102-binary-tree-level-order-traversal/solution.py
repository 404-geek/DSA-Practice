# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            temp = []

            for _ in range(len(q)):

                i = q.popleft()

                temp.append(i.val)
                
                if i.left:
                    q.append(i.left)
                if i.right:
                    q.append(i.right)

            res.append(temp)

        return res

        

                

            

        
