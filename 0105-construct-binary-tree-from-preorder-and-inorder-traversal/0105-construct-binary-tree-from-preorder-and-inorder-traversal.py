# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preorder_idx = 0
        self.inorder_idx_map = {}
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:       
        for i in range(len(inorder)):
            self.inorder_idx_map[inorder[i]] = i
            
        return self.arr_to_tree(0, len(preorder)-1, preorder)
    def arr_to_tree(self, left_idx, right_idx, preorder):
        if left_idx > right_idx:
            return None
        
        root_val = preorder[self.preorder_idx]
        root = TreeNode(root_val)
        
        self.preorder_idx += 1
        
        root.left = self.arr_to_tree(left_idx, self.inorder_idx_map[root_val]-1, preorder)
        root.right = self.arr_to_tree(self.inorder_idx_map[root_val]+1, right_idx, preorder)
        
        return root
        
        