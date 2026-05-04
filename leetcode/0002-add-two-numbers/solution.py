# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        
        head = ListNode()

        node = head

        while l1 or l2 or carry:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = carry + v1 + v2
            digit = total % 10
            carry = total // 10

            node.next = ListNode(digit)
            node = node.next

            if l1:
                l1  = l1.next
            if l2:
                l2  = l2.next

        return head.next



