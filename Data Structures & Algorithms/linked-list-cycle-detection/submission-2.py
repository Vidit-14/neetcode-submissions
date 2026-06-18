# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        while head.next != None:
            head.val = 'x'
            head = head.next

            if head.val == 'x':
                return True
        
        return False
        