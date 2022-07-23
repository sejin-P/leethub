# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        if root.left is None and root.right is None and targetSum == root.val:
            return [[root.val]]
        
        
        left = self.pathSum(root.left, targetSum-root.val)
        right = self.pathSum(root.right, targetSum-root.val)
        
        result = []
        for l in left:
            result.append([root.val]+l)
        for r in right:
            result.append([root.val]+r)
        
        return result
        