# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        res = []
        d = deque([(root, 0)])

        while d:
            node, level = d.popleft()
            if level >= len(res):
                if res:
                    res[-1] = sum(res[-1]) / len(res[-1])
                res.append([])
            
            res[-1].append(node.val)
            
            if node.left:
                d.append((node.left, level+1))
            if node.right:
                d.append((node.right, level+1))

        if len(res[-1]) >= 1:
            res[-1] = sum(res[-1]) / len(res[-1])
        
        return res


        