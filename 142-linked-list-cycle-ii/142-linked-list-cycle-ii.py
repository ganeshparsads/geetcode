# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # null check
        if not head:
            return None
        
        slow = head
        fast = head
        flag = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        
        if not flag:
            return None
        
        # resetting
        slow = head
        
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return slow
        