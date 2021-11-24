# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head
        p1 = p2 = temp
        
        for i in range(n):
            if p2.next:
                p2 = p2.next
            
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
            
        p1.next = p1.next.next
        return temp.next