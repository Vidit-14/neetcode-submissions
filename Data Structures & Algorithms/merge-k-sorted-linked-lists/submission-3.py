# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1: #breaks when length of list = 1 i.e when final list formed
            mergedLists = []

            for i in range(0, len(lists), 2): #2 hops since we are taking pairs of lists for merging
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2)) #we are appending address of heads of the merged lists
            
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        while l1:
            tail.next = l1
            l1 = l1.next
            tail = tail.next
        while l2:
            tail.next = l2
            l2 = l2.next
            tail = tail.next
        
        return dummy.next