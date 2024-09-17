# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preorder_idx = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def arr_to_tree(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            
            root_val = preorder[self.preorder_idx]
            root = TreeNode(root_val)
            
            self.preorder_idx += 1
            
            root.left = arr_to_tree(left_idx, inorder_idx_map[root_val]-1)
            root.right = arr_to_tree(inorder_idx_map[root_val]+1, right_idx)
            
            return root
            
        
        inorder_idx_map = {}
        for i in range(len(inorder)):
            inorder_idx_map[inorder[i]] = i
            
        return arr_to_tree(0, len(preorder)-1)
        