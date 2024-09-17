# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.rev_postorder_idx = 0
        self.rev_inorder_map = {}
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder.reverse()
        inorder.reverse()
        
        for i in range(len(inorder)):
            self.rev_inorder_map[inorder[i]] = i
            
        return self.arr_to_tree(0, len(postorder)-1, postorder)
    
    def arr_to_tree(self, right, left, rev_postorder):
        if right > left:
            return None
        
        root_val = rev_postorder[self.rev_postorder_idx]
        root = TreeNode(root_val)
        self.rev_postorder_idx += 1
        
        root.right = self.arr_to_tree(right, self.rev_inorder_map[root_val]-1, rev_postorder)
        root.left = self.arr_to_tree(self.rev_inorder_map[root_val]+1, left, rev_postorder)
        
        return root
    
        