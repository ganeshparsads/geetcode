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
        if head is None:
            return head
        
        curr = head
        
        while curr and curr.child is None:
            curr = curr.next
        
        if curr and curr.child:
            c_head = self.flatten(curr.child)
            
            curr.child = None
            
            ct_head = c_head
            
            while ct_head.next:
                ct_head = ct_head.next
            
            ct_head.next = curr.next
            
            if ct_head.next:
                ct_head.next.prev = ct_head
            
            curr.next = c_head
            
            curr.next.prev = curr

        return head
        
        
        
        