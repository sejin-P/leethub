# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # using ascii is simple but considering computation
        self.alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        li = self.getLeaves(root)
        
        return min(li)
        
    def getLeaves(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        
        l = self.getLeaves(root.left)
        r = self.getLeaves(root.right)
        
        al = self.alphabets[root.val]
        if len(r) == 0 and len(l) == 0:
            return [al]
        
        res = []
        for n in l:
            res.append(n+al)
        for n in r:
            res.append(n+al)
            
        return res
        
        
        