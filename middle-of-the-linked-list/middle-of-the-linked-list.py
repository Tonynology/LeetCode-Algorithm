# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head
        curr = fast = temp
        
        while fast.next and fast.next.next:
            curr = curr.next
            fast = fast.next.next
            
        head = curr.next
        
        return head