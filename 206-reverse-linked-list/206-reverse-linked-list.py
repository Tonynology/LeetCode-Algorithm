# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if (not head) or (not head.next):
            return head
        
        p = self.reverseList(head.next) # p is 5
        head.next.next = head # head is 4, head.next is 5
        head.next = None
        return p
        
#         prev = None
#         curr = head
        
#         while curr:
#             next_temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_temp
        
#         return prev
        