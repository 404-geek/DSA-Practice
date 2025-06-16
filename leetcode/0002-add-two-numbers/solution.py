# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        op = 1
        no1 = 0
        no2 = 0
        while l1 or l2:

            if l1:
                no1 += l1.val * op
                l1 = l1.next
            
            if l2:
                no2 += l2.val * op
                l2 = l2.next

            op *= 10


        n = no1 + no2

        if n == 0:
            return ListNode(0)
        
        head = None
        tail = None

        while n > 0:
            digit = n % 10
            node = ListNode(digit)

            if head is None:
                head = tail = node
            else:
                tail.next = node
                tail = node

            n //= 10
        return head

        
            

            
        
