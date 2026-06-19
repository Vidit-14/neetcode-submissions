# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        segments = length // k
        cur = head
        prev = None
        count = 0
        listHeads = []
        listTails = []
        while segments > 0:
            if prev == None:
                listHeads.append(cur)
        
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            count += 1

            if (count % k) == 0:
                segments -= 1
                listTails.append(prev)
                prev = None

        if cur:
            listTails.append(cur)
        
        for i in range(len(listTails) - 1):
            listHeads[i].next = listTails[i + 1] 
        
        return listTails[0]