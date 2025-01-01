"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        d = deque([(root, 0)])

        while d:
            nodeInfo = d.popleft()
            node, floor = nodeInfo[0], nodeInfo[1]
            if d and d[0][1] == floor:
                node.next = d[0][0]
            
            if node.left:
                d.append((node.left, floor+1))
            if node.right:
                d.append((node.right, floor+1))
        
        return root


        