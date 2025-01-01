# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preorder_idx = 0
        self.preorder = []
        self.inorder_idx_map = {}
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:   
        for i in range(len(inorder)):
            self.inorder_idx_map[inorder[i]] = i
        self.preorder = preorder

        return self.build(0, len(inorder)-1)
    
    def build(self, start_inorder_idx, end_inorder_idx):
        if start_inorder_idx > end_inorder_idx:
            return None
        val = self.preorder[self.preorder_idx]
        self.preorder_idx += 1
        n = TreeNode(val)

        now_inorder_idx = self.inorder_idx_map[val]
        n.left = self.build(start_inorder_idx, now_inorder_idx-1)
        n.right = self.build(now_inorder_idx+1, end_inorder_idx)

        return n

        