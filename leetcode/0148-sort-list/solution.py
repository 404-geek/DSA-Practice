# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow

            slow = slow.next
            fast = fast.next.next

        prev.next = None

        a = self.sortList(head)
        b = self.sortList(slow)

        dummy = ListNode()
        curr = dummy

        while a and b:

            if a.val <= b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            
            curr = curr.next

        if a:
            curr.next = a
        else:
            curr.next = b

        return dummy.next
            









        
