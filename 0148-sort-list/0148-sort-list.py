# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        n = head
        while n:
            li.append(n.val)
            n = n.next
        li.sort()
        
        l = head
        i = 0
        while l:
            l.val = li[i]
            l = l.next
            i += 1
        return head
        