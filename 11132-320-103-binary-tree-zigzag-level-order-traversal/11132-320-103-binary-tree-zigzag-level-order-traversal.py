# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d = deque([(root, 1)])
        prevOrder = 0
        res = []
        temp = deque([])

        while d:
            element = d.popleft()
            node, order = element[0], element[1]
            if prevOrder != order:
                if temp:
                    res.append(list(temp))
                prevOrder = order
                temp = deque([])
            
            if order:
                temp.append(node.val)
            else:
                temp.appendleft(node.val)
            
            if node.left:
                d.append((node.left, 1-order))
            if node.right:
                d.append((node.right, 1-order))
        
        if temp:
            res.append(list(temp))

        return res

                
            

                

        