"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return None

        q = deque([root])

        while q:

            a = len(q)
            prev = None
            for i in range(a):
                n = q.popleft()

                if prev:
                    prev.next = n
                prev = n
                
                if n.left:
                    q.append(n.left)

                if n.right:
                    q.append(n.right)

        return root




        
