# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res, _ = self.right(root, 0, -1)
        
        return res
        
    # return list int, depth
    def right(self, root, depth, shownDepth):
        if not root:
            return [], depth-1
        res = []
        if depth > shownDepth:
            shownDepth = depth
            res.append(root.val)
        
        r, m = self.right(root.right, depth+1, shownDepth)
        l, lm = self.right(root.left, depth+1, max(shownDepth, m))
        
        return res + r + l, max(shownDepth, lm, m)
        