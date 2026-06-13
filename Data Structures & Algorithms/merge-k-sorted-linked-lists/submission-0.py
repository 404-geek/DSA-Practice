# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        res = []

        for i, lis in enumerate(lists):

            heapq.heappush(res, (lis.val, i, lis))

        dummy = ListNode()
        curr = dummy

        while res:

            val, i, node = heapq.heappop(res)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(res, (node.next.val, i, node.next))

        return dummy.next



            

        





        