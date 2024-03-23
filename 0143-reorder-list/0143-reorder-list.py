# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        if not head.next:
            return None
        
        slow = head
        fast = head
        
        # find the mid
        while fast.next and fast.next.next:# fast.next for even and fast.next.next for odd
            slow = slow.next
            fast = fast.next.next
        
        # reverse the 2nd half
        fast = self.reversed(slow.next)
        # detach the tree
        slow.next = None
        
        slow = head
        # merge
        while fast:
            temp = slow.next
            slow.next = fast
            fast = fast.next
            slow.next.next = temp
            slow = temp
        
    
    def reversed(self, head):
        prev = None
        curr = head
        fast = head.next
        
        while fast:
            curr.next = prev
            prev = curr
            curr = fast
            fast = fast.next
        
        curr.next = prev
        return curr
