# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        len = 0
        res = head

        if not head:
            return None
        
        ptr = head
        while ptr:
            len += 1
            ptr = ptr.next
        
        ptr = head
        mid = len // 2
        while mid > 0:
            ptr = ptr.next
            mid -= 1
        
        curr = ptr.next
        ptr.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        p1 = head
        p2 = prev

        while head and prev:
            p1 = p1.next
            p2 = p2.next
            head.next = prev
            prev.next = p1
            head = p1
            prev = p2
        
        


        


        


        