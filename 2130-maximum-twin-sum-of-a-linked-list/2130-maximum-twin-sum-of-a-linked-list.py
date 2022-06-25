# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        li = []
        while head is not None:
            li.append(head.val)
            head = head.next
        max_sum = 0
        length = len(li)
        if length == 2:
            return sum(li)
        for i in range((length//2)):
            print(li[i])
            max_sum = max(max_sum, li[i]+li[length-1-i])
        return max_sum
        