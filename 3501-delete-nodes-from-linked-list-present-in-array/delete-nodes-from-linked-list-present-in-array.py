# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        dummy = ListNode()
        curr = dummy

        temp = head

        while temp:
            if temp.val not in nums:
                curr.next = temp
                curr = curr.next
            temp = temp.next

        curr.next = None

        return dummy.next


