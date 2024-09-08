"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h, l = self.flattenWithLast(head)
        
        return h
    
    def flattenWithLast(self, head: 'Optional[Node]') -> ('Optional[Node]', 'Optional[Node]'):
        if head is None:
            return None, None
        h = head
        
        l = None
        while h is not None:
            if h.child is None:
                l = h
                h = h.next
                continue
            
            flat, flatLast = self.flattenWithLast(h.child)
            h.child = None
            n = h.next
            
            h.next = flat
            flat.prev = h
            
            flatLast.next = n
            if n is not None:
                n.prev = flatLast
            
            l = flatLast
            h = n
        
        return head, l
        