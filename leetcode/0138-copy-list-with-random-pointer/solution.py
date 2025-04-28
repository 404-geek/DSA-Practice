"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        i = head
        random_dict = {None : None}
        while i:
            new = Node(i.val)
            random_dict[i] = new
            i = i.next

        i = head
        while i:
            new = random_dict[i]
            new.next = random_dict[i.next]
            new.random = random_dict[i.random]
            i = i.next

        return random_dict[head]

        




        


