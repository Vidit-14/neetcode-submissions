# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        len = 0
        ptr = head

        while ptr:
            len += 1
            ptr = ptr.next
        
        pos = len - n
        if pos == 0:
            head = head.next
            return head

        ptr = head
        while (pos - 1) > 0:
            ptr = ptr.next
            pos -= 1
        
        ptr.next = ptr.next.next

        return head


        