class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev, cur = None, head
            while cur:
                temp = cur.next
                cur.next = prev
                prev, cur = cur, temp
            return prev

        head = reverse(head)

        cur = head
        carry = 0
        while cur:
            num = cur.val * 2 + carry
            cur.val = num % 10
            carry = num // 10
            cur = cur.next

        if carry > 0:
            new_node = ListNode(carry)
            cur = head
            while cur.next:
                cur = cur.next
            cur.next = new_node

        return reverse(head)