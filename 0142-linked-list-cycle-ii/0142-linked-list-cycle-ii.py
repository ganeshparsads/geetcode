# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        flag = False
        fastNode = head
        slowNode = head
        
        while fastNode and fastNode.next:
            slowNode = slowNode.next
            fastNode = fastNode.next.next
            
            if slowNode == fastNode:
                flag = True
                break

        if not flag:
            return None
        
        slowNode = head
        
        while fastNode != slowNode:
            slowNode = slowNode.next
            fastNode = fastNode.next
        return slowNode