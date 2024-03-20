# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        slow , fast = head , head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = slow.next
        slow.next = None
        
        left_half = self.sortList(head)
        right_half = self.sortList(temp)

        dummy = ListNode()
        cur = dummy

        while left_half and right_half:
            if left_half.val < right_half.val:
                cur.next = left_half
                left_half = left_half.next
            else:
                cur.next = right_half
                right_half = right_half.next
            cur = cur.next
        cur.next = left_half or right_half

        return dummy.next