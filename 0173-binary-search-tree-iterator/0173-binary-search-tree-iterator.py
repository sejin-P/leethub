# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = self.convert(root)
        self.idx = 0
        
    def convert(self, root: Optional[TreeNode]):
        if not root:
            return []
        
        return self.convert(root.left) + [root.val] + self.convert(root.right)
        

    def next(self) -> int:
        res = self.arr[self.idx]
        self.idx += 1
        return res
        

    def hasNext(self) -> bool:
        return self.idx < len(self.arr)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()