# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        le = 0

        temp = head

        while temp:
            le+=1
            temp = temp.next

        ind_rem = le - n

        if ind_rem == 0:
            return head.next

        temp = head

        cnt = 0
        while temp:
            if cnt == ind_rem-1:
                temp.next = temp.next.next

            temp = temp.next
            cnt+=1

        return head
        
        




                


        
