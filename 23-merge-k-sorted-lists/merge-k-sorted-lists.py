# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # Filter out None elements
        lists = [lst for lst in lists if lst]

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        def mergeSort(lists, start, end):
            if start == end:
                return lists[start]
            mid = (start + end) // 2
            left = mergeSort(lists, start, mid)
            right = mergeSort(lists, mid + 1, end)
            return merge(left, right)

        def merge(list1, list2):
            if not list1:  
                return list2
            if not list2:
                return list1
            
            dummy = ListNode(0)
            res = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    res.next = list1
                    list1 = list1.next
                else:
                    res.next = list2
                    list2 = list2.next
                res = res.next

            if list1:
                res.next = list1
            if list2:
                res.next = list2

            return dummy.next

        return mergeSort(lists, 0, len(lists) - 1)
