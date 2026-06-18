# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2

        if not list2:
            return list1

        c1 = list1
        c2 = list2

        if list1.val <= list2.val:
            ptr = list1
            head = ptr
            c1 = c1.next
        else:
            ptr = list2
            head = ptr
            c2 = c2.next
        
        while c1 and c2:
            if c1.val <= c2.val:
                ptr.next = c1
                c1 = c1.next
                ptr = ptr.next
            else:
                ptr.next = c2
                c2 = c2.next
                ptr = ptr.next
        
        while c1:
            ptr.next = c1
            c1 = c1.next
            ptr = ptr.next
        
        while c2:
            ptr.next = c2
            c2 = c2.next
            ptr = ptr.next
        
        ptr.next = None
        return head
        