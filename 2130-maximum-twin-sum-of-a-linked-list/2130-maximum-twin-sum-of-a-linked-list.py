# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        stack = []
        
        while fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        stack.append(slow.val)
        slow = slow.next
        max_sum = 0
        while slow:
            twin = stack.pop()
            max_sum = max(max_sum, twin+slow.val)
            slow = slow.next
        return max_sum
        