# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_length(self, head):
        count = 0
        
        while head:
            head = head.next
            count += 1
        
        return count
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA = self.get_length(headA)
        lengthB = self.get_length(headB)

        diff = abs(lengthA - lengthB)
        if lengthA > lengthB:
            while diff:
                headA = headA.next
                diff -= 1
        elif lengthA < lengthB:
            while diff:
                headB = headB.next
                diff -= 1
        
        while headA:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
            
                