# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        stack = []
        preorder = []
        
        n = root
        while stack or n:
            while n:
                stack.append(n)
                preorder.append(n.val)
                n = n.left
            
            n = stack.pop()
            n = n.right
        
        ne = root
        for val in preorder[1:]:
            ne.left = None
            ne.right = TreeNode(val=val)
            ne = ne.right
        
        return root
        