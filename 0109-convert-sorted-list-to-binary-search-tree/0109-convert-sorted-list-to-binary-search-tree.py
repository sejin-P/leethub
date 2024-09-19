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
    def __init__(self):
        self.head = None
    def size(self, head: Optional[ListNode]) -> int:
        l = 0
        ptr = head
        while ptr:
            l += 1
            ptr = ptr.next
        
        return l
    
    def convert(self, l, r) -> Optional[TreeNode]:
        if l > r:
            return None
        
        mid = (l+r) // 2
        left = self.convert(l, mid-1)
        root = TreeNode(self.head.val)
        root.left = left
        self.head = self.head.next
        root.right = self.convert(mid+1, r)
        
        return root
        
        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
    
        while head:
            nums.append(head.val)
            head = head.next

        # 숫자 쫙 뽑아 주시고~

        def buildTree(sub):
            if len(sub) == 0:
                return None

            mid = len(sub) // 2
            node = TreeNode(val=sub[mid])

            node.left = buildTree(sub[:mid])
            node.right = buildTree(sub[mid+1:])

            return node
    
        return buildTree(nums)
    
    
        