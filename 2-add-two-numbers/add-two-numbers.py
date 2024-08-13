# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_node = ListNode(-1)

        node1 , node2 , carry , curr  = l1 , l2 , 0 , sum_node

        while node1 or node2 or carry:
            sm = (node1.val  if node1 else 0) + (node2.val if node2 else 0) + carry
            carry = sm // 10

            curr.next = ListNode(sm % 10)
            curr = curr.next
            node1 = node1.next if node1 else None
            node2  = node2.next if node2 else None

        if carry:
            curr.next = ListNode(carry)

        return sum_node.next