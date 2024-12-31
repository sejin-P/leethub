# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        prev = ListNode(-101, head)
        prevprev = ListNode(-101, prev)
        pp = prevprev
        p = prev

        modified = False
        while h:
            if prev.val == h.val:
                prevprev.next = h.next
                h = h.next
                modified = True
                continue
            if not modified:
                prevprev = prevprev.next
            else:
                modified = False
            prev = h
            h = h.next
        
        return pp.next if pp.next.val != -101 else p.next
        