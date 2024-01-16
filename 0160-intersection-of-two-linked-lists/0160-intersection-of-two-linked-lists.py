# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA and not headB:
            return None
        
        tempB = headB
        tempA = headA
        
        lenA = 0
        lenB = 0

        # calculate length
        while tempA:
            tempA = tempA.next
            lenA += 1

        # calculate length
        while tempB:
            tempB = tempB.next
            lenB += 1
        
        if lenA > lenB:
            tempA = headA
            for i in range(lenA - lenB):
                tempA = tempA.next
            tempB = headB
        else:
            tempB = headB
            for i in range(lenB - lenA):
                tempB = tempB.next
            tempA = headA

        while tempA:
            if tempA == tempB:
                return tempA
            
            tempA = tempA.next
            tempB = tempB.next

        return None