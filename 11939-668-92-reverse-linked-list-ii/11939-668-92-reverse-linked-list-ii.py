# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        prev = None
        h = head
        stack = []
        order = 1

        while order <= right:
            if order < left:
                prev = h
            else:
                stack.append(h.val)

            h = h.next
            order += 1

        if not prev:
            head = ListNode(stack.pop())
            prev = head
        
        while stack:
            prev.next = ListNode(stack.pop())
            prev = prev.next
        
        prev.next = h

        return head
            

            
        