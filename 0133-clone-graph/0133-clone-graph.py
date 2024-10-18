"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        n = Node(node.val)
        self.visited[node.val] = n
        
        for neighbor in node.neighbors:
            nn = self.visited.get(neighbor.val)
            if nn is None:
                nn = self.cloneGraph(neighbor)
                n.neighbors.append(nn)
            else:
                n.neighbors.append(nn)
        return n
        
        