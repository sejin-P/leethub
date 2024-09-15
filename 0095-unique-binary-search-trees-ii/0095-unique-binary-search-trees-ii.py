# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[] for _ in range(n+1)]
        dp[0] = [None]
        
        for i in range(1, n+1):
            for j in range(1, i+1):
                k = i - j
                for left in dp[j-1]:
                    for right in dp[k]:
                        dp[i].append(TreeNode(j, left, self.clone(right, j)))
        
        
        return dp[n]
    
    
    def clone(self, t: Optional[TreeNode], offset: int) -> Optional[TreeNode]:
        if not t:
            return None
        
        n = TreeNode(t.val+offset, None, None)
        n.left = self.clone(t.left, offset)
        n.right = self.clone(t.right, offset)
        
        return n
            