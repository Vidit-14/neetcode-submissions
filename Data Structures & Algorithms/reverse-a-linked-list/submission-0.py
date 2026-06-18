# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        prev = head
        curr = head.next
        last = head.next

        prev.next = None

        while last:
            last = last.next
            curr.next = prev
            prev = curr
            curr = last
        
        return prev