# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        self.ans = []
        
        def dfs(node, level, max_level):
            if node is None:
                return max_level
            if level > max_level:
                max_level = level
                self.ans.append(node.val)
            
            new_max_level = dfs(node.right, level+1, max_level)
            left_max_level = dfs(node.left, level+1, new_max_level)
            
            return left_max_level
        
        dfs(root, 1, 0)
        
        return self.ans
        