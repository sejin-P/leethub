# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMid(self, head: ListNode) -> ListNode:
        prevNode = None
        slowNode = head
        fastNode = head
        
        while fastNode and fastNode.next:
            prevNode = slowNode
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        
        if prevNode:
            prevNode.next = None
        
        return slowNode
        
        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        mid = self.findMid(head)
        
        root = TreeNode(mid.val)
        
        if mid == head:
            return root
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root
        