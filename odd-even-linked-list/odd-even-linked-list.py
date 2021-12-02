# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        h1 = h1_curr = head
        h2 = h2_curr = head.next
        
        while h1_curr.next and h2_curr.next:
            h1_curr.next = h2_curr.next
            h1_curr = h1_curr.next

            h2_curr.next = h1_curr.next
            h2_curr = h2_curr.next

        h1_curr.next = h2
        
        return h1
        
        
        
# h1curr.next = h2curr.next
# h1curr = h1curr.next
# h2curr.next = h1curr.next
# h2curr = h2.next