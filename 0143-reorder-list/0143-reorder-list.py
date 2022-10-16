# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle node
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow
        
        #reverse second part linked list
        prev = None
        curr2 = middle
        nextt = middle.next
        
        while nextt != None:
            curr2.next = prev
            prev = curr2
            curr2 = nextt
            nextt = nextt.next
        
        curr2.next = prev
        #curr is last node
        
        #merge two linked list
        curr1 = head
        temp1 = temp2 = None
        while curr2.next:
            
            temp1 = curr1.next
            curr1.next = curr2
            curr1 = temp1
            temp2 = curr2.next
            curr2.next = curr1
            curr2 = temp2
            
        return head
            