"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
            
        l_result = self.treeToDoublyList(root.left)
        r_result = self.treeToDoublyList(root.right)

        if l_result is None and r_result is None:
            root.left = root
            root.right = root
            return root
        
        if l_result is None:
            r_result.left.right = root
            root.left = r_result.left
            
            root.right = r_result
            r_result.left = root
            return root
        
        if r_result is None:
            l_result.left.right = root
            root.left = l_result.left
            
            root.right = l_result
            l_result.left = root
            return l_result
        
        l_result.left.right = root
        root.left = l_result.left
        
        r_result.left.right = l_result
        l_result.left = r_result.left
        
        root.right = r_result
        r_result.left = root
        
        
        return l_result
        