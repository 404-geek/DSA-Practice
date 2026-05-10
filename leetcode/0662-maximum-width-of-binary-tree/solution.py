# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return None
        
        wid = 1
        q = deque([(root, 0)])

        while q:

            level_len = len(q)
            _ , first_index = q[0]

            for _ in range(level_len):
                node, index = q.popleft()
                index-=first_index

                if node.left:
                    q.append((node.left, 2* index+1))
                
                if node.right:
                    q.append((node.right , 2* index + 2))

            wid = max(wid, index+1)

        return wid

                
                    



        
