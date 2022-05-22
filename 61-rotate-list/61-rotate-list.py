# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        li = []
        while head is not None:
            li.append(head.val)
            head = head.next
        
        n = len(li)
        
        k = k%n
        
        prevNode = ListNode(li[n-k-1])
        for i in range(n-k-2, -1, -1):
            newNode = ListNode(li[i], prevNode)
            prevNode = newNode
        
        for i in range(n-1, n-k-1, -1):
            newNode = ListNode(li[i], prevNode)
            prevNode = newNode
        
        return prevNode
        
        