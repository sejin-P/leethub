# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([(root, 0)])
        indexMap = defaultdict(list)
        
        while q:
            r = q.popleft()
            node, idx = r[0], r[1]
            if not node:
                continue
            
            indexMap[idx].append(node.val)
            
            q.append((node.left, idx-1))
            q.append((node.right, idx+1))
        
        keys = indexMap.keys()
        minIdx = min(keys)
        maxIdx = max(keys)
        
        for idx in range(minIdx, maxIdx+1):
            res.append(indexMap[idx])
            
        return res
        
        