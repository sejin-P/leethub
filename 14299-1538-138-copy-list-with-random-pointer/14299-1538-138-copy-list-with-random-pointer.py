"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        if head in self.visited:
            return self.visited[head]
        
        n = Node(head.val)

        self.visited[head] = n

        n.next = self.copyRandomList(head.next)
        n.random = self.copyRandomList(head.random)

        return n
        