# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
            
        q = deque([root])
        l_r = True
        ans = []

        while q:

            q_len = len(q)

            temp = []


            for n in range(q_len):
                
                a = q.popleft()

                temp.append(a.val)

                if a.left:
                    q.append(a.left)

                if a.right:
                    q.append(a.right)



            if not l_r:
                temp.reverse()
            
            ans.append(temp)
            l_r ^= 1
            

        return ans


                
        
