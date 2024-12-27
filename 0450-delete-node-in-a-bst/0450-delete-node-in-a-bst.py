# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val == key:
            if root.right:
                rightMostLeft = root.right
                while rightMostLeft and rightMostLeft.left:
                    rightMostLeft = rightMostLeft.left
                rightMostLeft.left = root.left
                return root.right
            else:
                return root.left
        
        if root.val < key:
            self.delete(root.right, root, key)
            return root
        
        self.delete(root.left, root, key)
        return root
                
        
    def delete(self, root, parent, key):
        if not root:
            return
        if root.val == key:
            if parent.val > key:
                if root.right:
                    rightMostLeft = root.right
                    while rightMostLeft and rightMostLeft.left:
                        rightMostLeft = rightMostLeft.left
                    rightMostLeft.left = root.left
                    parent.left = root.right
                else:
                    parent.left = root.left
            if parent.val < key:
                if root.left:
                    leftMostRight = root.left
                    while leftMostRight and leftMostRight.right:
                        leftMostRight = leftMostRight.right
                    leftMostRight.right = root.right
                    parent.right = root.left
                else:
                    parent.right = root.right
            return
        
        if root.val < key:
            return self.delete(root.right, root, key)
        return self.delete(root.left, root, key)
                    
        
        