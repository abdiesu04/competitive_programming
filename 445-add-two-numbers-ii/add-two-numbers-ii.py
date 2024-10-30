# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            cur = node

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        dummy  = ListNode()
        res  = None
        l1 = reverse(l1)
        l2 = reverse(l2)
        rem = 0
        while l1 or l2:
            val1  = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            v = val1 + val2 + rem
            rem = v // 10
            v %= 10

            newNode = ListNode(v)
            newNode.next = res
            res = newNode


            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if rem > 0:
            newNode = ListNode(rem)
            newNode.next = res
            res  = newNode

        return res

