# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        up = 0
        res = ListNode()
        h = res

        while l1 or l2:
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            
            if s + up >= 10:
                h.next = ListNode(s+up-10)
                up = 1
            else:
                h.next = ListNode(s+up)
                up = 0
            h = h.next

        if up:
            h.next = ListNode(1)
        return res.next
