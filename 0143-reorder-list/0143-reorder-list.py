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
        slow = head
        fast = head
        
        # middle of linked list
        # find the mid
        while fast.next and fast.next.next:# fast.next for even and fast.next.next for odd
            slow = slow.next
            fast = fast.next.next
        
        # reverse linked list
        head2 = self.reverseList(slow.next)

        slow.next = None
        
        slow = head
        
        # connect
        while head2:
            temp = head.next
            head.next = head2
            head2 = head2.next
            head.next.next = temp
            head = temp
            
        return head
        
            
    
    def reverseList(self, head) -> Optional[ListNode]:
        res = None
        
        while head:
            nxt = head.next
            head.next = res
            res = head
            head = nxt
        
        return res