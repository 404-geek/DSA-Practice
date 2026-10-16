# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        slow = head
        fast = head.next
        cnt = 1

        while fast:

            fast = fast.next   
            
            cnt+=1

        if cnt == n:
            return head.next

        ind = cnt - n - 1

        i = 0

        while i < ind:

            slow = slow.next
            i+=1

        rem = slow.next
        
        if not rem:
            pnt = None
        else:
            pnt = rem.next

        slow.next = pnt

        return head

        


        

